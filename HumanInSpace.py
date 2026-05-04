import requesting


#humans in space and what spacecraft they are in
def Human_space_info():
    astronauts = requesting.safe_request("http://api.open-notify.org/astros.json")
    
    person_list = []
    spacecraft = []

    if astronauts["message"] == "success":
        for astros in astronauts["people"]:
            person_list.append(f"\n{astros["name"]} on board {astros["craft"]}")
            if astros["craft"] in spacecraft:
                pass
            else:
                spacecraft.append(astros["craft"])
    else:
        print(f"something went wrong, API error message: {astronauts["message"]}")


    print(f"There are {astronauts["number"]} people in space\n")
    print(f"The people in space are:\n {''.join(person_list)}")
    print(f"\nThe current manned spacecraft in space are: {', '.join(spacecraft)}")
    


Human_space_info()
