from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(label="Nom Utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
	pwd = forms.CharField(label="Mot de Passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	
 