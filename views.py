import pandas as pd, json, re
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse, Http404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django_serverside_datatable.views import ServerSideDatatableView
from django_serverside_datatable import datatable
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from geopy.distance import distance
from .models import Rawtang, Rawramp, Rawkes,  ChartRaw, LocationActivity, SamplingSummary, SiteSampling, SamplingObservation,SamplingMeasurement, SampleCollection, SenderDetails, SampleDetails, SampleTransportation
from .forms import NewUserForm, ResetForm, RawtangForm, RawrampForm, RawkesForm, LogMasukForm, SamplingSummaryForm, SiteSamplingForm, SamplingObservationForm, SamplingMeasurementForm, SampleCollectionForm, SenderDetailsForm, SampleDetailsForm, SampleTransportationForm
from .serializers import RawtangSerializer, RawrampSerializer, RawkesSerializer, ChartRawSerializer

model_dict = {"rawtang":Rawtang,"rawramp":Rawramp,"rawkes":Rawkes,"sedar":LocationActivity,"summary":SamplingSummary,"site":SiteSampling,"observation":SamplingObservation,"measurement":SamplingMeasurement,"collection":SampleCollection,"sender":SenderDetails,"sample":SampleDetails,"transportation":SampleTransportation}

def sg_send_email(to_email, subject, html_content):
    message = Mail(from_email=settings.FROM_EMAIL,to_emails=to_email,subject=subject,html_content=html_content)
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        return str(e)

@login_required(redirect_field_name='next',login_url=reverse_lazy('app:login'))
def index(request):
    return render(request,"app/index.html")

@login_required(redirect_field_name='next',login_url=reverse_lazy('app:login'))
def data_entry(request):
    if request.method == 'POST':
        if "tablename" in request.POST:
            table_name = request.POST["tablename"]
            if table_name == "rantaianpenjagaan":
                sender_form = SenderDetailsForm(request.POST)
                sample_form = SampleDetailsForm(request.POST)
                transportation_form = SampleTransportationForm(request.POST)
                if sender_form.is_valid() and sample_form.is_valid() and transportation_form.is_valid():
                    sender_dict = sender_form.cleaned_data
                    sample_dict = sample_form.cleaned_data
                    transportation_dict = transportation_form.cleaned_data
                    SenderDetails(**sender_dict).save()
                    SampleDetails(**sample_dict).save()
                    SampleTransportation(**transportation_dict).save()
                    request_message = f"Data telah berjaya direkodkan di dalam jadual {table_name}"
            elif table_name == "fieldrecord":
                summary_form = SamplingSummaryForm(request.POST)
                site_form = SiteSamplingForm(request.POST)
                observation_form = SamplingObservationForm(request.POST, request.FILES)
                measurement_form = SamplingMeasurementForm(request.POST)
                collection_form = SampleCollectionForm(request.POST)
                if summary_form.is_valid() and site_form.is_valid() and observation_form.is_valid() and measurement_form.is_valid() and collection_form.is_valid():
                    weather_images = request.FILES.getlist('weather_images')
                    water_images = request.FILES.getlist('water_images')
                    observation_images = request.FILES.getlist('observation_images')
                    for weather_image in weather_images:
                        image_ins= SamplingObservation(Weather_Images = weather_image)
                        image_ins.save()
                    for water_image in water_images:
                        image_ins= SamplingObservation(Water_Images = water_image)
                        image_ins.save()
                    for observation_image in observation_images:
                        image_ins= SamplingObservation(Observation_Images = observation_image)
                        image_ins.save()
                    summary_dict = summary_form.cleaned_data
                    site_dict = site_form.cleaned_data
                    observation_dict = observation_form.cleaned_data
                    measurement_dict = measurement_form.cleaned_data
                    collection_dict = collection_form.cleaned_data
                    SamplingSummary(**summary_dict).save()
                    SiteSampling(**site_dict).save()
                    SamplingObservation(**observation_dict).save()
                    SamplingMeasurement(**measurement_dict).save()
                    SampleCollection(**collection_dict).save()
                    request_message = f"Data telah berjaya direkodkan di dalam jadual {table_name}"
            elif table_name == "rawtang":
                tableform = RawtangForm
                model = Rawtang
            elif table_name == "rawramp":
                tableform = RawrampForm
                model = Rawramp
            elif table_name == "rawkes":
                tableform = RawkesForm
                model = Rawkes
            form = tableform(request.POST)
            if form.is_valid():
                obj_dict = form.cleaned_data
                model(**obj_dict).save()
                request_message = f"Data telah berjaya direkodkan di dalam jadual {table_name}"
            else:
                request_message = f"Data gagal direkodkan di dalam jadual {table_name}"
            messages.success(request,request_message)
            return render(request=request, template_name=f"app/{table_name}_table.html")
    elif request.method == 'GET':
        context = dict()
        context['rawtang_form'],context['rawramp_form'],context['rawkes_form'],context['summary_form'],context['site_form'],context['observation_form'],context['measurement_form'],context['collection_form'],context['sender_form'],context['sample_form'],context['transportation_form'] = RawtangForm(),RawrampForm(),RawkesForm(),SamplingSummaryForm(),SiteSamplingForm(),SamplingObservationForm(),SamplingMeasurementForm(),SampleCollectionForm(),SenderDetailsForm(), SampleDetailsForm(), SampleTransportationForm()
        return render(request,"app/data_entry.html",context=context)

def user_login(request):
    if request.method == "POST":
        form = LogMasukForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Anda sedang log masuk sebagai {username}.")
                return HttpResponseRedirect(reverse('app:index'))
            else:
                messages.warning(request,"Nama pengguna atau kata laluan tidak didaftar.")
                return HttpResponseRedirect(reverse('app:login'))
        else:
            messages.warning(request,"Nama pengguna atau kata laluan tidak didaftar.")
            return HttpResponseRedirect(reverse('app:login'))
    else:
        form = LogMasukForm()
        return render(request=request, template_name="app/login.html", context={"login_form":form})

@login_required(redirect_field_name='next',login_url=reverse_lazy('app:login'))
def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"Registration successful.")
            return HttpResponseRedirect(reverse('app:index'))
        else:
            messages.warning(request,"Unsuccessful registration. Invalid information.")
            return HttpResponseRedirect(reverse('app:register'))
    else:
        form = NewUserForm()
        return render(request,"app/register.html",{"register_form":form})

def user_logout(request):
    logout(request)
    messages.success(request,"Anda telah log keluar.")
    return HttpResponseRedirect(reverse('app:login'))

def user_reset_pwd(request):
    if request.method == "POST":
        form = ResetForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email","")
            users = list(form.get_users(email))
            if users:
                form.save(email_template_name="app/password_reset_email.html",subject_template_name="app/password_reset_subject.txt",from_email="reeki@mfrlab.org",request=request)
                messages.success(request,"We have emailed the instructions for setting your password to the email you have entered. You should receive them shortly. If you do not receive an email, please make sure you have entered the address you have registered with, and check your spam folder.")
                return HttpResponseRedirect(reverse('app:login'))             
            else:
                form = ResetForm()
                messages.warning(request,"No user found registered with that email.")
                return render(request=request, template_name="app/password_reset.html", context={"reset_form":form})              
        else:
            form = ResetForm()
            messages.warning(request,"Invalid information.")
            return render(request=request, template_name="app/password_reset.html", context={"reset_form":form})
    else:
        form = ResetForm()
        return render(request=request, template_name="app/password_reset.html", context={"reset_form":form})

@login_required(redirect_field_name='next',login_url=reverse_lazy('app:login'))
def render_table(request,table_name):
    if request.method == "GET":
        action = request.GET.get("action")
        pk = request.GET.get("pk")
        if action == "del":
            messages.warning(request,"Fungsi untuk membuang rekod telah dinyahaktifkan.")
            return HttpResponseRedirect(reverse('app:table',kwargs={"table_name":table_name}))
        else:              
            return render(request=request, template_name=f"app/{table_name}_table.html")

class ServersideView(ServerSideDatatableView):
    def get_queryset(self):
        self.model = model_dict[self.kwargs['table_name']]
        queryset = self.model.objects.all() #_default_manager
        return queryset
    def get(self, request, *args, **kwargs):
        table_name = self.kwargs['table_name']
        column_names = [i.name for i in model_dict[table_name]._meta.fields]
        if self.kwargs['filtering'] == "on":
            self.columns = [i for i in column_names if i not in ["Nama","No_KP_Baru","No_KP_Lama","No_Paspot","Pegawai_Penyiasat"]]
        else:
            self.columns = column_names
        result = datatable.DataTablesServer(request, self.columns, self.get_queryset()).output_result()
        return JsonResponse(result, safe=False)

@login_required(redirect_field_name='next',login_url=reverse_lazy('app:login'))
def download(request,table_name):
    response = HttpResponse(
        headers = {
            "Content-Type": "text/csv",
            "Content-Disposition": f"attachment; filename={table_name}.csv",
        },
    )
    model = model_dict[table_name]
    table_dict = dict()
    for i in model.objects.values():
        for key in i.keys():
            if key != "id":
                if key not in table_dict.keys():
                    table_dict[key] = [i[key]]
                else:
                    table_dict[key].append(i[key])
    table_df = pd.DataFrame(table_dict)
    table_df.to_csv(path_or_buf=response,index=False)
    return response

def get_sedar(request):
    return render(request,"app/sedar_map.html")

def post_geotag(request):
    if request.method == "POST":
        latitude = request.POST['lat']
        longitude = request.POST['lng']
        data_dict = {"latitude":latitude,"longitude":longitude}
        crime_forms = request.POST.getlist('activities[]')
        activities = [i.name for i in LocationActivity._meta.fields[4:]]
        for activity in activities:
            re_str = activity.split("_")[0]
            if list(filter(lambda x:re.search(r""+re_str+"",x,flags=re.I),crime_forms)) != []:
                data_dict[activity] = "Ya"
            else:
                data_dict[activity] = "Tidak"
        if not LocationActivity(**data_dict).save():
            return JsonResponse({"message":"The reported data has been saved!"})
        else:
            return JsonResponse({"message":"There is an error while attempting to save the reported data!"})

def send_notification_email(area_coordinates): 
    subject = 'Notification: Exceeded Coordinates Threshold'
    message = f'The threshold for coordinates within a 500m radius has been exceeded.\n\n'
    message += 'Coordinates that triggered the threshold:\n'    
    for coordinate in area_coordinates:
       message += f'Coordinate : {coordinate}\n'
    recipient = 'nfitriyahbaharom@gmail.com'  #Replace with actual email 
    sg_send_email(recipient, subject, message)

def calculate_distance(coord1, coord2): 
    return distance((coord1.latitude, coord1.longitude), (coord2.latitude, coord2.longitude)).meters

def find_coordinates_with_distance(new_coord, existing_coord, area_lists): 
    for area_coordinates in area_lists:
        for existing_coord in area_coordinates:
            dist = calculate_distance(new_coord, existing_coord)
            if dist <= 500:
                area_coordinates.append(new_coord)
                area_coordinates.append(existing_coord)
        unique_area_coordinates = list(set(area_coordinates))
        if len(unique_area_coordinates) >= 10:
            return unique_area_coordinates
    new_area_list = [new_coord]
    area_lists.append(new_area_list)
    return None

def handle_coordinates(request):
    coordinates = LocationActivity.objects.all().values('lat', 'lng')
    area_lists = []
    if request.method == 'POST' and request.is_ajax():
        lat = float(request.POST.get('lat'))
        lng = float(request.POST.get('lng'))
        new_coord = LocationActivity(latitude=lat, longitude=lng)
        new_coord.save()
        area_coordinates = find_coordinates_with_distance(new_coord, coordinates, area_lists)
        print(area_coordinates)
        if area_coordinates is not None:
            send_notification_email(area_coordinates)
        response_data = {
            'message': 'Data received and processed successfully!',
            'latitude': lat,
            'longitude': lng,
        }
        return JsonResponse(response_data)
    else: 
        return JsonResponse({'error': 'Invalid request'})
    
class RawtangViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication,)
    queryset = Rawtang.objects.all().order_by('id')
    serializer_class = RawtangSerializer

class RawrampViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication,)
    queryset = Rawramp.objects.all().order_by('id')
    serializer_class = RawrampSerializer

class RawkesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication,)
    queryset = Rawkes.objects.all().order_by('id')
    serializer_class = RawkesSerializer

class ChartRawList(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication,)
    def get(self, request, format=None):
        raws = ChartRaw.objects.all().order_by('-Update_timestamp')
        serializer = ChartRawSerializer(raws, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        print(request.data)
        serializer = ChartRawSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChartRawDetail(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication,)
    def get_object(self, pk):
        try:
            return ChartRaw.objects.get(pk=pk)
        except ChartRaw.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        raw = self.get_object(pk)
        serializer = ChartRawSerializer(raw)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        raw = self.get_object(pk)
        serializer = ChartRawSerializer(raw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        raw = self.get_object(pk)
        raw.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
