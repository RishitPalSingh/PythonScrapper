from src.scrapped_to_database import create_table,scrape_website_table
from src.create_csv import export_to_csv
from src.crud import fetch_data,edit_MAN_by_Basis,delete_row_by_Basis,fetch_Basis


def main():
    


    while True:
        print("1. scrape data ")
        print("2. create csv")
        print("3. read data")
        print("4. delete sample")
        print("5. update table")
        print("6. exiting program")

        choice = input("Enter your choice (1/2/3/4/5/6): ")


        if choice=='1':
            url = "https://www.geeksforgeeks.org/difference-between-lan-man-and-wan/"
            scrape_website_table(url)
        elif choice =="2":
            export_to_csv()
        elif choice =="3":
            fetch_data()
        elif choice =="4":
            fetch_Basis()
            sample=input("enter your basis which you want to delete: ")

            delete_row_by_Basis(sample)
        elif choice =="5":
            fetch_data()
            Basis_to_edit = input("enter the basis of which MAN you want to change: ")
            column_to_edit= input("select LAN/ MAN/ WAN: ")
            New_MAN=input(f"Enter Updated {column_to_edit} : ")
            edit_MAN_by_Basis(Basis_to_edit,column_to_edit,New_MAN)
        elif choice=="6":
            print("exiting...")
            break








main()