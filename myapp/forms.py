from django import forms

class MovieForm(forms.Form):

    title=forms.CharField()

    options=(
        ("Action","Action"),
        ("Fiction","Fiction"),
        ("Drama","Drama"),
        ("Comedy","Comedy"),
    )

    genre=forms.ChoiceField(choices=options)

    language=forms.CharField()

    year=forms.CharField()

    run_time=forms.IntegerField()

    director=forms.CharField()


    def clean(self):
        # call parent class clean()

        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")

        if int(year)<1900:

            error_messasge="ENTER THE MOVIE RELEASE AFTER 1900"

            self.add_error("year",error_messasge)

        if run_time>210:

            error_messasge="run time is invalid"

            self.add_error("run_time",error_messasge)


        if run_time<60:

            error_messasge="run time is invalid"

            self.add_error("run_time",error_messasge)
            
        
    

