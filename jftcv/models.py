from django.db import models 
 
class PersonalData(models.Model): 
    name = models.CharField(max_length=50) 
    initials=models.CharField(primary_key=True,max_length=8) 
    address = models.CharField(max_length=50) 
    city = models.CharField(max_length=50)
    code = models.CharField(max_length=10) 
    country = models.CharField(max_length=30) 
    phonenumber = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    datebirth = models.CharField(max_length=20)
    nationality = models.CharField(max_length=30)
    profile = models.CharField(max_length=600,blank=True)
    linkedin = models.URLField(blank=True) 
    github = models.URLField(blank=True) 
    
    class Meta: 
        verbose_name_plural = "Personal data" 
        
    def __str__(self): 
         return str(self.name)+"("+str(self.initials)+")"

class WorkExperience(models.Model): 
    owner = models.CharField(max_length=50,verbose_name='user')
    dates = models.CharField(max_length=60) 
    position = models.CharField(max_length=70) 
    organization = models.CharField(max_length=90)
    description = models.CharField(max_length=120,blank=True) 
    
    class Meta: 
        verbose_name_plural = "Work experiences" 
        
    def __str__(self): 
         return str(self.position)

class Education(models.Model): 
    owner = models.CharField(max_length=50,verbose_name='user')
    dates = models.CharField(max_length=60) 
    title = models.CharField(max_length=70) 
    organization = models.CharField(max_length=90)
    description = models.CharField(max_length=120,blank=True) 
    certificate = models.URLField(blank=True) 
    
    class Meta: 
        verbose_name_plural = "Trainings" 
        
    def __str__(self): 
         return str(self.title)

class Conferences(models.Model): 
    owner = models.CharField(max_length=50,verbose_name='user')
    dates = models.CharField(max_length=60) 
    title = models.CharField(max_length=70) 
    organization = models.CharField(max_length=90)
    description = models.CharField(max_length=120,blank=True)
    
    class Meta: 
        verbose_name_plural = "Conferences and events" 
        
    def __str__(self): 
         return str(self.title)


class Projects(models.Model): 
    owner = models.CharField(max_length=50,verbose_name='user') 
    name = models.CharField(max_length=50,verbose_name='Project name') 
    language = models.CharField(max_length=50,verbose_name='Programming language')
    filename = models.CharField(max_length=50,verbose_name='Folder (inside the django application)',blank=True)
    url = models.URLField(blank=True) 
    
    class Meta: 
        verbose_name_plural = "Projects" 
        
    def __str__(self): 
         return str(self.name)


class Languages(models.Model): 
    owner = models.CharField(max_length=50,verbose_name='user')
    language = models.CharField(max_length=50,verbose_name='Language')
    written = models.CharField(max_length=10,verbose_name='Written (level)')
    spoken = models.CharField(max_length=10,verbose_name='Spoken (level)')
    understood = models.CharField(max_length=10,verbose_name='Understood (level)')
    native = models.CharField(max_length=10,verbose_name='Native language (Yes/No)')
    
    class Meta: 
        verbose_name_plural = "Languages" 
        
    def __str__(self): 
         return str(self.language)


class DigComps(models.Model): 
    owner = models.CharField(max_length=50,verbose_name='user')
    comp = models.CharField(max_length=50,verbose_name='Digital competence')
    infoprocessing = models.CharField(max_length=10,verbose_name='Information processing (level)')
    contentcreation = models.CharField(max_length=10,verbose_name='Content creation (level)')
    safety = models.CharField(max_length=10,verbose_name='Safety (level)')
    problemsolving = models.CharField(max_length=10,verbose_name='Problem solving (level)')
    
    class Meta: 
        verbose_name_plural = "Digital competences" 
        
    def __str__(self): 
         return str(self.comp)

class Router(models.Model):
    owner = models.CharField(max_length=50,verbose_name='user') 
    specifications = models.FileField(upload_to='router_specifications')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        verbose_name_plural = "CV file"


class ImgProfile(models.Model):
    owner = models.CharField(max_length=50,verbose_name='user') 
    specifications = models.FileField(verbose_name='Picture (.png)')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        verbose_name_plural = "Profile image" 


if __name__=="__main__":
    javi=PersonalData(name="Javier Fernández Troncoso",initials="jft",address="17 Meadowbank St.",city="Belfast - Northern Ireland", code="BT9 7FG",country="United Kingdom",phonenumber="+34 633 507 590", mail="javierfdeztroncoso@gmail.com", datebirth="19/08/1992",nationality="Spanish, Portuguese", linkedin="https://www.linkedin.com/in/javier-fern%C3%A1ndez-troncoso-7ba743112/", github="https://javifdezt.github.io/", profile="Information technology professional trained to participarte in technology projects with remarkable deadline sensitivity. Experience as a software developer with python, java and unix. Stron analytical, mathematical and statistical skills obtained through university period, including a stay abroad. Compatible team player through complete project cycles, testing and final implementation. Knowledge of foreign languages, driving licence, availability to travel in and outside the country.")
    javi.save()

    gft1=WorkExperience(dates="August  2015 – June 2016", position="Release manager – BIG DATA Project", organization="GFT IBERIA,  c/ Orduña, 1;  28034 Madrid; Spain   -    gft.com",description="Managing the process of planning, scheduling and controlling the software build through different stages and environments; Code review; Deployments, automation. Deployment tools: SVN, GIT, Teamcity, Putty, Oracle SQL developer...",certificate="")
    gft2=WorkExperience(dates="June  2016 – September 2016", position="SL3 Team member – BIG DATA Project", organization="GFT IBERIA,  c/ Orduña, 1;  28034 Madrid; Spain   -    gft.com",description="Technical support to Production. High level; Deployments in production",certificate="")
    phd=WorkExperience(dates="September 2016 - Today", position="PhD student", organization="Atomistic Simulation Centre,  School of Physics and Mathematics, Queen's University, Belfast.",description="Simulations with Python; Thermoelectricity",certificate="")
    gft1.save()
    gft2.save()
    phd.save()

    degree=Education(dates="September  2010  - June 2014", title="Degree: Physics", organization="University of Santiago de Compostela; Santiago de Compostela, Spain ",description="Physics; Mathematics and  statistics; Programming: Python, Matlab; Data analysis; Regressions: performance of economy", certificate="")
    master=Education(dates="September  2014  - June 2015", title="Master's degree: Science and technology of materials", organization="University of Santiago de Compostela; Santiago de Compostela, Spain ",description="Materials; Statistics; Programming: Python; Data analysis; Simulation", certificate="")
    javagft=Education(dates="June 2015  - July 2015", title="Certificate course: Java Training", organization="LUZ Tecnologías de la Información; Madrid, Spain",description="Java; SQL; HTML", certificate="")
    ibmfoundations=Education(dates="August 2015", title="BIG DATA – Foundations", organization="IBM; Online",description="Big Data", certificate="https://www.youracclaim.com/badges/cb97cb1a-1bb3-482d-ad37-57c6abcf584a/linked_in_profile")
    ibmhadoop=Education(dates="August 2015", title="BIG DATA – Hadoop foundations", organization="IBM; Online",description="Big Data; Hadoop", certificate="https://www.youracclaim.com/badges/cb8898c8-c7c3-43ec-9668-75968afb8a37/linked_in_profile")
    ibmprogramming=Education(dates="August 2015", title="BIG DATA – Programming", organization="IBM; Online",description="Big Data; Hadoop; Hive", certificate="https://www.youracclaim.com/badges/b9751948-e5fa-4635-811e-7789c567c27f/linked_in_profile")
    linux=Education(dates="January 2016", title="Certificate course: Introduction to LINUX  (Linux FoundationX - LFS101x.2)", organization="Linux Foundation; Online",description="Linux", certificate="https://verify.edx.org/cert/807a017bc17e43beb3b84556dc4d6655; https://s3.amazonaws.com/verify.edx.org/downloads/12f5fef76cdb44759afb3434ba788647/Certificate.pdf")
    hadoop=Education(dates="June 2016", title="Certificate course: DEV 301 - Developing Hadoop Applications", organization="MapR Technologies; Online",description="Big Data; Hadoop; Hive", certificate="https://verify.skilljar.com/c/7ptnmrxgi8an")
    degree.save()
    master.save()
    javagft.save()
    ibmfoundations.save()
    ibmhadoop.save()
    ibmprogramming.save()
    linux.save()
    hadoop.save()

    pybel1=Conferences(dates="26th October  2016", title="Pybelfast - Meeting", organization="Farset Labs, Belfast",description="Django vs Rails; Extending python withrust and cffi")
    gle=Conferences(dates="13th-14th January  2017", title="Generalised Langevin Equation: Theory and Applications", organization="King's College London, London",description="Generalised Langevin Equation")
    atk=Conferences(dates="24th January  2017", title="How Atoms Move: Introduction to Molecular Dynamics Simulations with VNL and ATK-Classical", organization="Webinar online -  QuantumWise (Denmark)",description="Molecular dynamics; Python")
    pybel1.save()
    gle.save()
    atk.save()

    l1=Languages(owner="Javier Fernández Troncoso", language="Spanish",writen="Proficient",spoken="Proficient", understood="Proficient",native="Yes")
    l2=Languages(owner="Javier Fernández Troncoso", language="Galician",writen="Proficient",spoken="Proficient", understood="Proficient",native="Yes")
    l3=Languages(owner="Javier Fernández Troncoso",language="Portuguese",writen="Basic",spoken="Independient", understood="Proficient",native="No")
    l4=Languages(owner="Javier Fernández Troncoso",language="English",writen="Independient",spoken="Independient", understood="Independient",native="No")
    l1.save()
    l2.save()
    l3.save()
    l4.save()

    c1=DigComps(owner="Javier Fernández Troncoso", comp="Java",infoprocessing="Independient",contentcreation="Basic", safety="Basic",problemsolving="Independient")
    c2=DigComps(owner="Javier Fernández Troncoso", comp="Python",infoprocessing="Independient",contentcreation="Proficient", safety="Basic",problemsolving="Proficient")
    c3=DigComps(owner="Javier Fernández Troncoso", comp="SQL",infoprocessing="Independient",contentcreation="Basic", safety="Basic",problemsolving="Independient")
    c4=DigComps(owner="Javier Fernández Troncoso", comp="Hadoop",infoprocessing="Independient",contentcreation="Basic", safety="Basic",problemsolving="Independient")
    c5=DigComps(owner="Javier Fernández Troncoso", comp="Office",infoprocessing="Independient",contentcreation="Independient", safety="Proficient",problemsolving="Proficient")
    c6=DigComps(owner="Javier Fernández Troncoso", comp="Linux",infoprocessing="Independient",contentcreation="Independient", safety="Independient",problemsolving="Independient")
    c7=DigComps(owner="Javier Fernández Troncoso", comp="Windows",infoprocessing="Independient",contentcreation="Independient", safety="Independient",problemsolving="Basic")
    c8=DigComps(owner="Javier Fernández Troncoso", comp="Matlab",infoprocessing="Independient",contentcreation="Basic", safety="Basic",problemsolving="Independient")
    c9=DigComps(owner="Javier Fernández Troncoso", comp="Django",infoprocessing="Independient",contentcreation="Independient", safety="Basic",problemsolving="Independient")
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    c5.save()
    c6.save()
    c7.save()
    c8.save()
    c9.save()


