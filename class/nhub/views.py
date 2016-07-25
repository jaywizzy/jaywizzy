from django.shortcuts import render
from django.http import HttpResponse
from nhub.models import Users

# Create your views here.
def jay(request):
	return HttpResponse("<h1> welcome to my world.......JAYWIZZY</h1>")
def junior(request):
	return HttpResponse("<body style='background-color:orange'> whad up fellas</body>")
def shergzie(request):
	# user= Users.objects.get(first_name="jay").first_name
	wizzy=	'''
			<html>
				<head>
					<title></title>
					<style type="tex/css">
						aside{display:block;}
						header ul li a:{
						color:green;
						}
						header li:{color:blue;}

					</style>
				</head>
				<body style="background-color:red">
					<header id="header">
						<ul>
							<li><a>home</a></li>
							<li><a>login</a></li>
							<li><a>contact<a/></li>
							<li><a>register</a></li>

						</ul>
					</header>
					<section style="background-color:green">
							<image src="/home/oluwashegun/Desktop/image/‪+234 708 134 6305‬ 20151026_154340.jpg" height="500" width="500">

					fjv jf bvfjbvfvf
					</section>
					<aside>
							<image src="/home/oluwashegun/Desktop/image/‪+234 708 134 6305‬ 20151026_154340.jpg" height="500" width="500">
					</aside>
					<footer> &copy nhub hosting 2016	</footer>
				


				</body>

			</html>
			'''
			# %(user)
	return HttpResponse(wizzy)

	