#!/usr/bin/python2

import os
i=1
print "            this is a resume builder tool in python."



choice1="""To secure a position where i can efficiently contribute my skills and abilities to the growth of the organization and build my professional career."""


choice2="""To associate with a vibrant organization, to fully utilize my knowledge,skills and contribute to the overall growth of the organization."""






while(i<2):
	os.system("tput setaf 1")
	print "fill all the fields to make a professional resume."
	os.system("tput setaf 0")
	os.system("tput setaf 2")
	print """\n
	         1. Contact   Information
		 2. Carrer    Objective
		 3. Education Qualification
		 4. Technical Skills
		 5. Training  Attended
		 6. Extracurricular Activity
		 7. AchiveMents
		 8. Project
		 9. Make my resume
		10.view resume.
	      """
	os.system("tput setaf 0")
	os.system("tput setaf 1")
	ch=raw_input("enter your choice:-")
	os.system("tput setaf 0")
	if int(ch)==1:
		os.system("tput setaf 1")
		print "\n\ngive some contact information of you."
		os.system("tput setaf 0")
		name=raw_input("Name:- ")
		Email=raw_input("Email:- ")
		Phone=raw_input("Mobile Number:- ")
		#Dob=raw_input("Date of Birth(dd/mm/yyyy):-")
		#Gender=raw_input("Gender(male/female):-")
 		#Married=raw_input("Married/Unmarried:-")

	elif int(ch)==2:
		os.system("tput setaf 1")
		print "\n\nselect any career objective or make your own."
		os.system("tput setaf 0")
		print"""\n1.To secure a position where i can efficiently contribute my skills and abilities to
			    the growth of the organization and build my professional career.
			\n2.To associate with a vibrant organization, to fully utilize my knowledge,skills and 
			    contribute to the overall growth of the organization.
		      \n\n3.make your own.
			"""
		selectoption=raw_input("select any option:-")
	
		if int(selectoption)==1:
			choice=choice1
		elif int(selectoption)==2:
			choice=choice2
		elif int(selectoption)==3:
			choice=raw_input("write from here:-")

		else:
			print "select right option."



	elif int(ch)==3:
		os.system("tput setaf 1")
		print "\nenter education qualification here."
		os.system("tput setaf 0")
		btech=raw_input("graduation(B.Tech/M.Tech):- ")
		stream=raw_input("stream(CS/IT/EEE/ME:-")
		college=raw_input("college(skit jaipur):- ")
		bpercentage=raw_input(btech+"percentage(75%):- ")
		byear=raw_input(btech+"year of passing(2019):- ")
		twelth=raw_input("12th board(CBSE/RBSE):- ")
		tpercentage=raw_input("12th percentage/cgpa:- ")
		tyear=raw_input("12th year of passing(2014):- ")
		tenth=raw_input("10th board(CBSE/RBSE):- ")
		tenpercentage=raw_input("10th percentage/cgpa:- ")
		tenyear=raw_input("10th year of passing(2012):- ")
		
	


	elif int(ch)==4:
		os.system("tput setaf 1")
		print "enter your technical skills."
		os.system("tput setaf 0")
		soft=raw_input("software language(c,c++,java,python..):- ")
		app=raw_input("computer application(Ms Office,Excel,Powerpoint....):- ")
		tech=raw_input("technologies(hadoop,oracle,mysql...):- ")
		other=raw_input("others:- ")

		

	elif int(ch)==5:
		os.system("tput setaf 1")
		print "enter your traning information here."
		os.system("tput setaf 0")
		company=raw_input("enter the company name from you attended traning:- ")
		month=raw_input("training period(2 month):- ")
		onwhich=raw_input("on which technoloy/language/other:- ")


	elif int(ch)==6:
		os.system("tput setaf 1")
		print "enter your extracurricular activity here."
		os.system("tput setaf 0")
		extra=raw_input("enter something for extracurricular activities:- ")

	elif int(ch)==7:
		os.system("tput setaf 1")
		print "enter your achievements here."
		os.system("tput setaf 0")
		achieve=raw_input("enter your achievement/certifications:- ")
		
	elif int(ch)==8:
		os.system("tput setaf 1")
		print "enter your project information here."
		os.system("tput setaf 0")
		project=raw_input("enter project name:- ")
		description=raw_input("description for project:- ")
		
		
	elif int(ch)==9:
		fh=open("/root/Desktop/resume1.txt","w")
		fh.write("                                 Resume")
		fh.write("\n\nName:-"+name)
		fh.write("\nEmail:-"+Email)
		fh.write("\nMobile:-"+Phone)
		fh.write("\n_________________________________________________________________________________")
		fh.write("\n\nCAREER OBJECTIVE:-")
		fh.write("\n\n"+choice)
		fh.write("\n_________________________________________________________________________________")
		fh.write("\n\nEDUCATION QUALIFICATION:-")
		fh.write("\n\n"+btech+" in "+stream+" from "+college+" Affiliated by RTU kota.")
		fh.write("\n|______________________|________________________|_______________|")
		fh.write("\n| Degree/Examination   | Institute/University   | Percentage    | Year")
		fh.write("\n|______________________|________________________|_______________|")
		fh.write("\n| "+btech+"               |"+college+"             |"+bpercentage+"            |"+byear)
		fh.write("\n|"+twelth+"                  |12th                    |"+tpercentage+"            |"+tyear)
		fh.write("\n|"+tenth+"                  |10th                    |"+tenpercentage+"            |"+tenyear)
		fh.write("\n_________________________________________________________________________________")
		fh.write("\n\nTECHNICAL SKILLS:-")
		fh.write("\n\nsoftware language:-"+soft)
		fh.write("\ncomputer application:-"+app)
		fh.write("\ntechnologies:-"+tech)
		fh.write("\nothers:-"+other)
		fh.write("\n_________________________________________________________________________________")
		fh.write("\n\nTRAINING ATTENDED:-")
		fh.write("\n\nAttended training from "+company+" for "+month+" on "+onwhich)
		fh.write("\n_________________________________________________________________________________")		
		fh.write("\n\nEXTRACURRICULAR ACTIVIES:-")
		fh.write("\n\n"+extra)
		fh.write("\n_________________________________________________________________________________")
		fh.write("\n\nACHIEVEMENTS/CERTIFICATIONS:-")
		fh.write("\n\n"+achieve)
		fh.write("\n_________________________________________________________________________________")
		fh.write("\n\nPROJECTS:-")
		fh.write("\n\nproject name:-"+project)
		fh.write("\ndescription:-"+description)
		fh.write("\n_________________________________________________________________________________")
		fh.close()

	elif int(ch)==10:
		os.system("gedit /root/Desktop/resume1.txt")	
	else:
		print "enter correct option."

raw_input()
