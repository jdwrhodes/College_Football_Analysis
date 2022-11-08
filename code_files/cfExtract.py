import pandas as pd

#This function is used to import a List of Dataframes and then slice out the "Name" column and remove the Conference portion at the end and put it in it's own column next to it. Then it reinserts the "Name" column without the Conference name.
def conferenceExtract(DataFrameList):
    import pandas as pd
    def add_value(dict_obj, key, value):
        if key not in dict_obj:
            dict_obj[key] = value
        elif isinstance(dict_obj[key], list):
            dict_obj[key].append(value)
        else:
            dict_obj[key] = [dict_obj[key], value]

    iterator = 0
    no_conf_name = {}

    for i in DataFrameList:
        df=pd.DataFrame(DataFrameList[iterator])
        teams = list(df.Team)
        conf_only = []
        team_only = []

        for x in teams:
            conf_only.append(x[x.find('(')+1:x.find(')')])

            if x[x.find('(')+1:x.find(')')] == "":
                add_value(no_conf_name, iterator, x)
            
            x = x.split("(", 1)[0]
            team_only.append(x)

        df.insert(loc = 1,
                    column = 'Conference',
                    value = conf_only)
        
        team_only = pd.DataFrame(team_only)
        
        df["Team"] = team_only[0]
        
        iterator+=1