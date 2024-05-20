from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.forms import RadioSelect, CheckboxSelectMultiple, Select

from .models import Rawtang, Rawramp, Rawkes, SamplingSummary, SiteSampling, SamplingObservation, SamplingMeasurement, SampleCollection, SenderDetails, SampleDetails, SampleTransportation

class TextAndRadioMultiValueField(forms.MultiValueField):
    def __init__(self, choices, *args, **kwargs):
        fields = (
			forms.ChoiceField(choices=choices),
            forms.CharField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return data_list

class TextAndRadioMultiWidget(forms.MultiWidget):
    def __init__(self, choices,placeholder=None, attrs=None ):
        widgets = (
            forms.RadioSelect(choices=choices),
            forms.TextInput(attrs={'placeholder':placeholder}),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value
        return [None, None]
	
class TextAndSelectMultiValueField(forms.MultiValueField):
	def __init__(self, choices, *args, **kwargs):
		fields = (
			forms.ChoiceField(choices=choices),
			forms.CharField()
		)
		super().__init__(fields, *args, **kwargs)
	
	def compress(self, data_list):
		return data_list

class TextAndSelectMultiWidget(forms.MultiWidget):
	def __init__(self, choices, placeholder=None, attrs=None):
		widgets = (
			forms.CheckboxSelectMultiple(choices=choices),
			forms.TextInput(attrs={'placeholder':placeholder}),
		)
		super().__init__(widgets, attrs)
	
	def decompress(self,value):
		if value:
			return value
		return [None,None]

class DatePickerInput(forms.DateInput):
	input_type = 'date'

class TimePickerInput(forms.TimeInput):
	input_type = 'time'

class RadioTextFieldWidget(forms.MultiWidget):
	def __init__(self,attrs=None, choices=None):
		widgets = [forms.RadioSelect(choices=choices,attrs=attrs), forms.TextInput(attrs=attrs)]
		super().__init__(widgets,attrs)

	def decompress(self, value):
		if value:
			return [value[0],value[1]]
		return [None, '']

	def format_output(self, rendered_widgets):
		return '<br>'.join(rendered_widgets)


	
class LogMasukForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Nama Pengguna'
        self.fields['password'].label = 'Kata Laluan'

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2",)

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ResetForm(PasswordResetForm):
	email = forms.EmailField(label=_("Email"),max_length=254,required=True)

	class Meta:
		model = User
		fields = ("email",)

class RawtangForm(forms.ModelForm):
	class Meta:
		model = Rawtang
		fields = "__all__"
		#exclude = ('No_KS',)

class RawrampForm(forms.ModelForm):
	class Meta:
		model = Rawramp
		fields = "__all__"

class RawkesForm(forms.ModelForm):
	class Meta:
		model = Rawkes
		fields = "__all__"

# Field Record Form 
class SamplingSummaryForm(forms.ModelForm):
	class Meta:
		model = SamplingSummary
		fields = "__all__"
		labels = {
			"Sampler_Name" : "Nama Pensampel",
			"Project_No" : "No. Projek",
			"Sampling_Date" : "Tarikh Pensampelan",
			"Sampling_Begin_Time" : "Waktu Mula Pensampelan",
			"Sampling_End_Time" : "Waktu Tamat Pensampelan",
		}
		widgets = {
			"Sampling_Date" : DatePickerInput() ,
			"Sampling_Begin_Time" : TimePickerInput(),
			"Sampling_End_Time" :  TimePickerInput(),
		}

class SiteSamplingForm(forms.ModelForm):
	class Meta:
		model = SiteSampling
		fields = "__all__"
		labels = {
			"Site_ID" : "ID Tapak",
			"GPS" : "GPS",
			"Location" : "Lokasi",
			"Postcode" : "Poskod",
			"Photo_No" : "No. Gambar",
		}

class SamplingObservationForm(forms.ModelForm):

	Weather_Images = forms.FileField(widget=forms.TextInput(attrs={
		"name" : "weather_images",
		"type" : "File",
		"class" : "form-control",
		"multiple" : "True",
	}), label = "CUACA - Gambar", required= False, )

	Water_Images = forms.FileField(widget=forms.TextInput(attrs={
		"name" : "water_images",
		"type" : "File",
		"class" : "form-control",
		"multiple" : "True",
	}), label = "AIR - Gambar", required= False)

	Observation_Images = forms.FileField(widget=forms.TextInput(attrs={
		"name" : "observation_images",
		"type" : "File",
		"class" : "form-control",
		"multiple" : "True",
	}), label = "PEMERHATIAN - Gambar", required= False)
	


	class Meta:
		windDirection_choices = [('Utara', 'Utara (U)'),
						     ('Timur', 'Timur (T)'),
							 ('Selatan','Selatan (S)'),
							 ('Barat','Barat (B)'),
							 ('Timur Laut','Timur Laut (TL)'),
							 ('Tenggara','Tenggara (TG)'),
							 ('Barat Daya','Barat Daya (BD)'),
							 ('Barat Laut','Barat Laut(BL)'),
							 ('Utara Timur Laut','Utara Timur Laut (UTL)'),
							 ('Timur Timur Laut', 'Timur Timur Laut (TTL)'),
							 ('Timur Tenggara','Timur Tenggara (TTG)'),
							 ('Selatan Tenggara','Selatan Tenggara (STG)'),
							 ('Selatan Barat Daya','Selatan Barat Daya (SBD)'),
							 ('Barat Barat Daya','Barat Barat Daya (BBD)'),
							 ('Barat Barat Laut','Barat Barat Laut (BBL)'),
							 ('Utara Barat Laut','Utara Barat Laut (UBL)'),
							 ('Berubah-ubah','Berubah-ubah')]
		
		CloudCover_choices = [('Tiada Awan','Tiada Awan'),
							('Sedikit Awan','Sedikit Awan (10-25%)'),
							('Separa Mendung','Separa Berawan (25-50%)'),
							('Kebanyakan Mendung','Kebanyakan Berawan (50-75%)'),
							('Berawan Mendung','Berawan/Mendung (75-100%)')]
		
		RainIntensity_choices = [('Tiada Hujan','Tiada Hujan'),
						   		('Renyai','Renyai'),
								('Sederhana Lebat','Sederhana Lebat'),
								('Lebat','Lebat'),
								('Sangat Lebat','Sangat Lebat')]
		
		Tide_choices = [('Air Pasang','Air Pasang'),
				  		('Air Surut','Air Surut')]
		
		FlowDirection_choices = [('Dari hulu ke hilir','Dari Hulu Ke Hilir'),
						   		('Dari utara ke selatan','Dari Utara Ke Selatan'),
								('Dari selatan ke utara','Dari Selatan ke Utara'),
								('Dari barat ke timur','Dari Barat Ke Timur'),
								('Dari timur ke barat','Dari Timur Ke Barat'),
								('Tidak menentu','Tidak Menentu')]
		
		ChoppyMixedCalm_choices = [('Tenang','Tenang'),
							 	('Berombak Sederhana','Berombak Sederhana'),
								('Bergelora','Bergelora'),
								('Berubah-ubah','Berubah-ubah')]
		
		Colour_choices = [('Jernih','Jernih'),
						('Keruh','Keruh'),
						('Kecoklatan','Kecoklatan'),
						('Kehijauan','Kehijauan'),
						('Kebiruan','Kebiruan'),
						('Kuning','Kuning'),
						('Merah','Merah'),
						('Hitam','Hitam'),
						('Lain-lain','Lain-lain')]
		
		SurfaceFilm_choices = [('Ada','Ada'),
						 	('Tiada','Tiada')]

		AlgaeDebris_choices = [('Alga','Alga'),
						 	('Fitoplankton','Fitoplankton'),
							('Serpihan','Serpihan')]
		
		OdourType_choices = [('Tiada Bau','Tiada Bau'),
							('Kimia','Kimia (bau pelarut/cat/pencemaran kimia dll)'),
							('Organik','Organik (bau tumbuhan/haiwan/bangkai)'),
							('Busuk','Busuk (bau pereputan/pembusukan organik/air kotor dll)'),
							('Gas Beracun','Gas Beracun (bau gas asid/gas petrol dll)'),
							('Tumpahan Minyak','Tumpahan Minyak (bau tumpahan minyak/pelinciran)'),
							('Berangus','Berangus (bau asap/pembakaran kayu/sisa pembakaran dll)'),
							('Manis','Manis (bau manis makanan/minuman/bahan kimia dll)'),
							('Bahan Pembersih','Bahan Pembersih (bau klorin/peluntur/pembersih rumah dll)'),
							('Urin','Urin (bau urin haiwan/manusia)'),
							('Lain-lain','Lain-lain')]
		
		OdourIntensity_choices = [('Tidak Berbau','Tidak Berbau'),
								('Lembut','Lembut'),
								('Sederhana','Sederhana'),
								('Kuat','Kuat'),
								('Sangat Kuat','Sangat Kuat'),
								('Berubah-ubah','Berubah-ubah')]

		model = SamplingObservation
		exclude = ('SiteSampling_ID',)
		labels = {
			"Weather_Temp" : "CUACA - Suhu",
			"Weather_WindSpeed" : "CUACA - Kelajuan Angin (km/j)",
			"Weather_WindDirection" : "CUACA - Arah Angin",
			"Weather_CloudCover" : "CUACA - Litupan Awan",
			"Weather_RainIntensity" : "CUACA - Kelebatan Hujan",
			"Weather_RainDuration" : "CUACA - Tempoh Hujan",
			"Weather_Note" : "CUACA - Catatan Tambahan",
			"Weather_Images" : "CUACA - Gambar",
			"Water_Tide" : "AIR - Air Pasang",
			"Water_Depth" : "AIR - Kedalaman Air (m)",
			"Water_FlowVelocity" : "AIR - Halaju Aliran Air (m/s)",
			"Water_FlowDirection" : "AIR - Arah Aliran Air",
			"Water_ChoppyMixedCalm" : "AIR - Keadaan Air",
			"Water_Colour" : "AIR - Warna Air",
			"Water_Note" : "AIR - Catatan Tambahan",
			"Water_Images" : "AIR - Gambar",
			"Observation_SurfaceFilm" : "PEMERHATIAN - Filem Permukaan Air",
			"Observation_Algae_Debris" : "PEMERHATIAN - Alga/Fitoplankton/Serpihan",
			"Observation_OdourType" : "PEMERHATIAN - Jenis Bau",
			"Observation_OdourIntensity" : "PEMERHATIAN - Kekuatan Bau",
			"Additional_Observation" : "PEMERHATIAN - Catatan Tambahan",
			"Observation_Images" : "PEMERHATIAN - Gambar",
			
		}
		widgets = {
			"Weather_WindDirection" : Select(choices=windDirection_choices),
			"Weather_CloudCover" : Select(choices=CloudCover_choices),
			"Weather_RainIntensity" : Select(choices=RainIntensity_choices),
			"Water_Tide" : Select(choices=Tide_choices),
			"Water_FlowDirection" : Select(choices=FlowDirection_choices),
			"Water_ChoppyMixedCalm" : Select(choices=ChoppyMixedCalm_choices),
			"Water_Colour" : Select(choices=Colour_choices),
			"Observation_SurfaceFilm" : RadioSelect(choices=SurfaceFilm_choices),
			"Observation_Algae_Debris" : CheckboxSelectMultiple(choices=AlgaeDebris_choices),
			"Observation_OdourType" : Select(choices=OdourType_choices),
			"Observation_OdourIntensity" : Select(choices=OdourIntensity_choices),
		}

class SamplingMeasurementForm(forms.ModelForm):
	class Meta:
		model = SamplingMeasurement
		exclude = ('SiteSampling_ID',)
		labels = {
			"Temp_result" : "SUHU - Hasil Pengukuran",
			"Temp_instrument" : "SUHU - Alat Pengukur",
			"DissolvedOxygen_result" : "OKSIGEN TERLARUT - Hasil Pengukuran",
			"DissolvedOxygen_instrument" : "OKSIGEN TERLARUT - Alat Pengukur",
			"Turbidity_result" : "KEKERUHAN - Hasil Pengukuran",
			"Turbidity_instrument" : "KEKERUHAN - Alat Pengukur",
			"Conductivity_result" : "KEKONDUKSIAN - Hasil Pengukuran",
			"Conductivity_instrument" : "KEKONDUKSIAN - Alat Pengukur",
			"pH_result" : "pH - Hasil Pengukuran",
			"pH_instrument" : "pH - Alat Pengukur",
			"Chlorine_result" : "KLORIN - Hasil Pengukuran",
			"Chlorine_instrument" : "KLORIN - Alat Pengukur",
		}


class SampleCollectionForm(forms.ModelForm):
	class Meta:
		model = SampleCollection
		exclude = ('Sampling_ID', 'SiteSampling_ID',)
		labels = {
			"Sample_No" : "No. Sampel",
			"Sample_Notes" : "Catatan",
		}

#Chain of Custody Form
class SenderDetailsForm(forms.ModelForm):
	class Meta:
		model = SenderDetails
		fields = "__all__"
		labels = {
			"Sender_Name" : "Nama Pengirim",
			"Laboratory" : "Makmal",
			"Case_No" : "No. Kes",
			"Contact_Name" : "Nama Kontak",
			"Reference_No" : "No. Rujukan",
			"Address" : "Alamat Makmal/Pejabat",
			"Contact" : "No. Telefon Pejabat/Makmal",
			"Phone_No1" : "No. Telefon (1)",
			"Phone_No2" : "No. Telefon (2)",
		}

class SampleDetailsForm(forms.ModelForm):
	class Meta:
		model = SampleDetails
		exclude = ('Sender_ID',)
		labels = {
			"Sample_ID" : "ID Sampel",
			"Sample_Location" : "Lokasi",
			"Sample_Date" : "Tarikh",
			"Sample_Time" : "Masa",
			"Container_Type" : "Jenis Bekas",
			"Container_Size" : "Saiz Bekas (mL)",
			"Container_Preservatives" : "Bahan Pengawet",
			"AnalysisRequired_HeavyMetal" : "Logam Berat",
			"AnalysisRequired_Toxicity" : "Ketoksikan",
			"Remarks" : "Catatan",
		}
		widgets = {
			"AnalysisRequired_HeavyMetal" : RadioSelect(choices=[
				(True, 'Ada'),
				(False, 'Tiada')
			]),
			"AnalysisRequired_Toxicity" : RadioSelect(choices=[
				(True, 'Ada'),
				(False, 'Tiada')
			]),
			"Sample_Date" : DatePickerInput(),
			"Sample_Time" : TimePickerInput(),

		}

class SampleTransportationForm(forms.ModelForm):
	class Meta:
		model = SampleTransportation
		exclude = ('SampleTransported_ID',)
		labels = {
			"Send_SamplerName" : " PENSAMPEL - KURIER HANTAR - Nama Pensampel",
			"Send_SamplerIC" : "HANTAR - No. KP Pensampel",
			"Send_SamplerDate" : "HANTAR - Tarikh Serahan Sampel (Pensampel)",
			"Send_SamplerTime" : "HANTAR - Masa Serahan Sampel (Pensampel)",
			"Receive_CourierName" : "TERIMA - Nama Kurier",
			"Receive_CourierIC" : "TERIMA - No. KP Kurier",
			"Receive_CourierDate" : "TERIMA - Tarikh Terima Sampel (Kurier)", 
			"Receive_CourierTime" : "TERIMA - Masa Terima Sampel (Kurier)", 
			"Receive_CourierSampleCond" : "TERIMA - Keadaan Sampel (Kurier)",
			"Sampler_Courier_AgreedCondition" : "Keadaan Sampel Dipersetujui Pensampel-Kurier (suhu/tidak pecah/dll)",
			"Send_CourierName" : "HANTAR - Nama Kurier",
			"Send_CourierIC" : "HANTAR - No. KP Kurier", 
			"Send_CourierDate" : "HANTAR - Tarikh Hantar Sampel (Kurier)", 
			"Send_CourierTime" : "HANTAR - Masa Hantar Sampel (Kurier)", 
			"Receive_LabName" : "TERIMA - Nama Penerima/Makmal", 
			"Receive_LabIC" : "TERIMA - No. KP Penerima/Makmal",
			"Receive_LabDate" : "TERIMA - Tarikh Terima Sampel (Makmal)",
			"Receive_LabTime" : "TERIMA - Masa Terima Sampel (Makmal)", 
			"Receive_LabSampleCond" : "TERIMA - Keadaan Sampel (Makmal)", 
			"Courier_Lab_AgreedCondition" : "Keadaan Sampel Dipersetujui Kurier-Makmal (suhu/tidak pecah/dll)"
		}
		widgets = {
			"Send_SamplerDate" : DatePickerInput(),
			"Send_SamplerTime" : TimePickerInput(),
			"Receive_CourierDate" : DatePickerInput(),
			"Receive_CourierTime" : TimePickerInput(),
			"Send_CourierDate" : DatePickerInput(),
			"Send_CourierTime" :  TimePickerInput(),
			"Receive_LabDate" :DatePickerInput(),
			"Receive_LabTime" :  TimePickerInput(),
		
		}
