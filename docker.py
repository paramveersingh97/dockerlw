import os

def images(a):
    while True:
        os.system("tput setaf 3")
        print("-------------------------------------------------------------------------------")
        os.system("tput setaf 7")
        print("""
        Press 1 : to show all images
        Press 2 : to pull image
        Press 3 : to remove image 
        Press 4 : to go back
        """)
        print("\n")
        img_choice = int(input("Enter your choice : "))
        if img_choice == 1:
            os.system("docker images")
        elif img_choice == 2:
            img=input("Enter the name of your image : ")
            os.system(f"docker pull {img}")
        elif img_choice == 3:
            rm_img=input("Enter name of the image to remove : ")
            os.system("tput setaf 1")
            print("Are you sure want to remove the image ")
            os.system("tput setaf 7")
            yes_no = input("y/n : ")
            if yes_no == 'y':
                os.system(f"docker rmi {rm_img}")
            if yes_no == 'n':
                pass
                
        elif img_choice == 4:
            break
        else:
            print("Please enter correct choice") 


def containers(b):
    while True:
        os.system("tput setaf 3")
        print("-------------------------------------------------------------------------------")
        os.system("tput setaf 7")
        print("""
        Press 1 : to show all containers
        Press 2 : to lauch conatiner in foreground 
        Press 3 : to attach conatiner
        Press 4 : to inspect any conatiner 
        Press 5 : to commit conatiner 
        Press 6 : to run command in the conatiner 
        Press 7 : to install any software/package
        Press 8 : to start/stop conatiner
        Press 9 : to rm conatiner 
        Press 10 : to go back 
        """)
        print("\n")
        con_choice = int(input("Enter your choice : "))
        if con_choice == 1:
            os.system("docker ps -a")
        elif con_choice == 2:
            os.system("tput setaf 2")
            print("""Press ctrl + p + q to deattach the conatiner
            Print exit to stop tha conatiner""")
            os.system("tput setaf 7")
            image_name=input("Enter image name : ")
            name = input("Enter container name : ")
            os.system(f"docker run -it  --name {name} {image_name}")
        elif con_choice == 3:
            os.system("tput setaf 2")
            print("""Press ctrl + p + q to detaach the conatiner
            Print exit to stop tha conatiner""")
            os.system("tput setaf 7")
            name = input("Enter container name : ")
            os.system(f"docker attach {name}")
        elif con_choice == 4:
            name = input("Enter container name : ")
            os.system(f"docker inspect {name}")
        elif con_choice == 5:
            name_source = input("Enter container name : ")
            name_con = input("Enter container name : ")
            os.system(f"docker commit {name_source} {name_con}")
        elif con_choice == 6:
            name = input("Enter container name : ")
            command=input("What command you want to run")
            os.system(f"docker exec {name} {command}")
        elif con_choice == 7:
            name = input("Enter container name : ")
            soft_name =input("Enter software name  : ")
            os.system(f"docker exec {name} yum install {sof_name}")
        elif con_choice == 8:
            name=input("Enter conatiner name : ")
            start_stop=input("""what do you want?
            start/stop, please eneter""")
            if start_stop == "start":
                os.system(f"docker start {name}")
            elif start_stop == "stop":
                os.system(f"docker stop {name}")
        elif con_choice == 9:
            name = input("Enter name of the container : ")
            os.system(f"docker rm $(docker stop {name})")
        elif con_choice == 10:
            break
        else:
            print("Please enter correct choice")


def network(c):
    while True:
        os.system("tput setaf 3")
        print("-------------------------------------------------------------------------------")
        os.system("tput setaf 7")

        print("""
        Press 1 : to create network
        Press 2 : to show all networks
        Press 3 : to inspect network
        Press 4 : to disconnect container from a n/w
        Press 5 : to connect conatiner to n/w
        Press 6 : to remove a network
        Press 7 : to prune all unused network
        Press 8 : to go back
        """)

        nw_choice=int(input("enter your choice : "))
        
        if nw_choice == 1:
            nw_name=input("Enter the name of network : ")
            driver_name=input("enter the driver name : ")
            os.system(f"docker network create --driver {driver_name} {nw_name}")
        elif nw_choice == 2:
            os.system("docker network ls")
        elif nw_choice == 3:
            nw_name=input("Enter name of the network : ")
            os.system(f"docker inspect {nw_name}")
        elif nw_choice == 4:
            nw_name=input("Enter name of the netwrok : ")
            con_name=input("enter name of the container : ")
            os.system(f"docker network disconnect {nw_name} {con_name}")
        elif nw_choice == 5:
            nw_name=input("Enter name of the netwrok : ")
            con_name=input("enter name of the container : ")
            os.system(f"docker network connect {nw_name} {con_name}")
        elif nw_choice == 6:
            nw_name =input("Enter n/w name : ")
            os.system(f"docker network rm {nw_name}")
        elif nw_choice == 7:
            os.system("docker network prune")
        elif nw_choice == 8:
            break
        else:
            print("Please enter correct choice")


def volume(d):
    while True:
        os.system("tput setaf 3")
        print("-------------------------------------------------------------------------------")
        os.system("tput setaf 7")
        
        print("""
        Press 1 : to create volume
        Press 2 : to show all volumes
        Press 3 : to inspect volume
        Press 4 : to remove volume
        Press 5 : to prune all unused volumes
        Press 6 : to go back
        """)

        vol_choice=int(input("Enter your choice : "))

        if vol_choice == 1:
            name=input("Enter name of volume : ")
            os.sytem("docker volume create {name}")
        elif vol_choice == 2:
            os.system("docker volume ls")
        elif vol_choice == 3:
            name=input("Enter name : ")
            os.system(f"docker inspect {name}")
        elif vol_choice == 4:
            name=input("Enter name : ")
            os.system(f"docker rm {name}")
        elif vol_choice == 5:
            os.system("docker volume prune")
        elif vol_choice == 6:
            break
        else:
            print("Please enter correct choice")

 





os.system("tput setaf 3")
print("***************************** Welcome to containerization **********************")
os.system("tput setaf 7")
print("\n\n")

while True:
    print("-------------------------------------------------------------------------------")
    print("""
    Press 1 : images
    Press 2 : containers
    Press 3 : network
    Press 4 : volume
    Press 5 : exit
    """)
    choice = int(input("Enter your choice : " ))

    if choice == 1:
        images(choice)
    elif choice == 2 :
        containers(choice)
    elif choice == 3:
        network(choice)
    elif choice == 4 :
        volume(choice)
    elif choice == 5:
        exit()

