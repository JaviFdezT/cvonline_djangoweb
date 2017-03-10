from django.shortcuts import render
from django.http import Http404
from os import listdir 
import os
from os.path import isfile, join
from jftcv.models import PersonalData,Projects,WorkExperience,Conferences,Education,Languages,DigComps,Router,ImgProfile

def cv(request,initialsofname):
    cvpath="."
    onlyfiles = [f for f in listdir(cvpath) if isfile(join(cvpath, f))]
    if "index.html" not in onlyfiles:
        raise Http404() 
    else:
      variables={}
      try:
        person=PersonalData.objects.get(initials=str(initialsofname))
        address=[person.address,str(person.code)+" "+str(person.city),person.country]
        
        personaldata={"myname":person.name,"myaddress":address,"mymail":person.mail,
		"mydatebirth":person.datebirth,"myphonenumber":person.phonenumber,
		"mynationality":person.nationality,"mylinkedin":person.linkedin,"mygithub":person.github}

        projects=Projects.objects.filter(owner=str(person.initials)).order_by("name")
        projectdata={"myprojects":[i for i in projects]}

        works=WorkExperience.objects.filter(owner=str(person.initials)).order_by("-id")
        workdata={"myworks":[i for i in works]}

        educs=Education.objects.filter(owner=str(person.initials)).order_by("-id")
        educdata={"myeducs":[i for i in educs]}

        confs=Conferences.objects.filter(owner=str(person.initials)).order_by("-id")
        confdata={"myconfs":[i for i in confs]}

        langs=Languages.objects.filter(owner=str(person.initials)).order_by("-native")
        langdata={"mylangs":[i for i in langs]}
        
        digcomps=DigComps.objects.filter(owner=str(person.initials)).order_by("comp")
        digcompdata={"mydigcomps":[i for i in digcomps]}
        
        try: 
          cvfile=Router.objects.filter(owner=str(person.initials))[0]
          cvfiledata={"cvfile":cvfile.specifications}
        except IndexError: cvfiledata={"cvfile":""}

        try: 
          imgfile=ImgProfile.objects.filter(owner=str(person.initials))[0]
          imgfiledata={"imgfile":imgfile.specifications}
        except IndexError: imgfiledata={"imgfile":""}


        variables.update({"person":person})
        variables.update(personaldata)
        variables.update(projectdata)
        variables.update(workdata)
        variables.update(educdata)
        variables.update(confdata)
        variables.update(langdata)
        variables.update(digcompdata)
        variables.update(cvfiledata)
        variables.update(imgfiledata)
      except PersonalData.DoesNotExist: 
        raise Http404()
      site=render(request, 'index.html',variables) 
      return site 






