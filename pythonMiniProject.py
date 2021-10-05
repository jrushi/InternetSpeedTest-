import speedtest


st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:

1) Download Speed

2) Upload Speed


Your Choice: '''))


if option == 1:

	print(st.download()/1000000,"Mbps")

elif option == 2:

	print(st.upload()/1000000,"Mbps")


else:

	print("Please enter the correct choice !")
