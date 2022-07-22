# region Model-Table
# region Model-Table-C1_Fuschia_D2L1_MyWork_Entity1_Category_List
class C1_Fuschia_D2L1_MyWork_Entity1_Category_List_Table():
    Entity1Category_Name = None
    Entity1Category_Name_Unique = None
    Entity1Category_ID = None
    Record_DateTime = None
    Upgrade_DateTime = None

    def __init__(self,Entity1Category_Name = None,Entity1Category_Name_Unique = None,Entity1Category_ID = None,Record_DateTime = None,Upgrade_DateTime = None):
        self.Entity1Category_Name = Entity1Category_Name
        self.Entity1Category_Name_Unique = Entity1Category_Name_Unique
        self.Entity1Category_ID = Entity1Category_ID
        self.Record_DateTime = Record_DateTime
        self.Upgrade_DateTime = Upgrade_DateTime

    def Read_DataFrameToClassObjects(DataFrame):
        return [(C1_Fuschia_D2L1_MyWork_Entity1_Category_List_Table(
            row.Entity1Category_Name,
            row.Entity1Category_Name_Unique,
            row.Entity1Category_ID,
            row.Record_DateTime,
            row.Upgrade_DateTime
        )) for index, row in DataFrame.iterrows() ]
# endregion
# region Model-Table-C1_Fuschia_D2L1_MyWork_Entity2_Category_List
class C1_Fuschia_D2L1_MyWork_Entity2_Category_List_Table():
    Entity2Category_Name = None
    Entity2Category_Name_Unique = None
    Entity2Category_ID = None
    Record_DateTime = None
    Upgrade_DateTime = None

    def __init__(self,Entity2Category_Name = None,Entity2Category_Name_Unique = None,Entity2Category_ID = None,Record_DateTime = None,Upgrade_DateTime = None):
        self.Entity2Category_Name = Entity2Category_Name
        self.Entity2Category_Name_Unique = Entity2Category_Name_Unique
        self.Entity2Category_ID = Entity2Category_ID
        self.Record_DateTime = Record_DateTime
        self.Upgrade_DateTime = Upgrade_DateTime

    def Read_DataFrameToClassObjects(DataFrame):
        return [(C1_Fuschia_D2L1_MyWork_Entity2_Category_List_Table(
            row.Entity2Category_Name,
            row.Entity2Category_Name_Unique,
            row.Entity2Category_ID,
            row.Record_DateTime,
            row.Upgrade_DateTime
        )) for index, row in DataFrame.iterrows() ]
# endregion
# region Model-Table-C1_Fuschia_D2L1_MyWork_Entity3_Category_List
class C1_Fuschia_D2L1_MyWork_Entity3_Category_List_Table():
    Entity3Category_Name = None
    Entity3Category_Name_Unique = None
    Entity3Category_ID = None
    Record_DateTime = None
    Upgrade_DateTime = None

    def __init__(self,Entity3Category_Name = None,Entity3Category_Name_Unique = None,Entity3Category_ID = None,Record_DateTime = None,Upgrade_DateTime = None):
        self.Entity3Category_Name = Entity3Category_Name
        self.Entity3Category_Name_Unique = Entity3Category_Name_Unique
        self.Entity3Category_ID = Entity3Category_ID
        self.Record_DateTime = Record_DateTime
        self.Upgrade_DateTime = Upgrade_DateTime

    def Read_DataFrameToClassObjects(DataFrame):
        return [(C1_Fuschia_D2L1_MyWork_Entity3_Category_List_Table(
            row.Entity3Category_Name,
            row.Entity3Category_Name_Unique,
            row.Entity3Category_ID,
            row.Record_DateTime,
            row.Upgrade_DateTime
        )) for index, row in DataFrame.iterrows() ]
# endregion
# region Model-Table-C1_Fuschia_D2L1_MyWork_Entity1_List
class C1_Fuschia_D2L1_MyWork_Entity1_List_Table():
    User_ID = None
    Application_ID = None
    Entity1Category_ID = None
    Entity1_Name = None
    Entity1_Desc = None
    Entity1_Name_Unique = None
    Entity1_ID = None
    Record_DateTime = None
    Upgrade_DateTime = None

    def __init__(self,User_ID = None,Application_ID = None,Entity1Category_ID = None,Entity1_Name = None,Entity1_Desc = None,Entity1_Name_Unique = None,Entity1_ID = None,Record_DateTime = None,Upgrade_DateTime = None):
        self.User_ID = User_ID
        self.Application_ID = Application_ID
        self.Entity1Category_ID = Entity1Category_ID
        self.Entity1_Name = Entity1_Name
        self.Entity1_Desc = Entity1_Desc
        self.Entity1_Name_Unique = Entity1_Name_Unique
        self.Entity1_ID = Entity1_ID
        self.Record_DateTime = Record_DateTime
        self.Upgrade_DateTime = Upgrade_DateTime

    def Read_DataFrameToClassObjects(DataFrame):
        return [(C1_Fuschia_D2L1_MyWork_Entity1_List_Table(
            row.User_ID,
            row.Application_ID,
            row.Entity1Category_ID,
            row.Entity1_Name,
            row.Entity1_Desc,
            row.Entity1_Name_Unique,
            row.Entity1_ID,
            row.Record_DateTime,
            row.Upgrade_DateTime
        )) for index, row in DataFrame.iterrows() ]
# endregion
# region Model-Table-C1_Fuschia_D2L1_MyWork_Entity2_List
class C1_Fuschia_D2L1_MyWork_Entity2_List_Table():
    Entity1_ID = None
    Entity2Category_ID = None
    Entity2_Name = None
    Entity2_Desc = None
    Entity2_Name_Unique = None
    Entity2_ID = None
    Record_DateTime = None
    Upgrade_DateTime = None

    def __init__(self,Entity1_ID = None,Entity2Category_ID = None,Entity2_Name = None,Entity2_Desc = None,Entity2_Name_Unique = None,Entity2_ID = None,Record_DateTime = None,Upgrade_DateTime = None):
        self.Entity1_ID = Entity1_ID
        self.Entity2Category_ID = Entity2Category_ID
        self.Entity2_Name = Entity2_Name
        self.Entity2_Desc = Entity2_Desc
        self.Entity2_Name_Unique = Entity2_Name_Unique
        self.Entity2_ID = Entity2_ID
        self.Record_DateTime = Record_DateTime
        self.Upgrade_DateTime = Upgrade_DateTime

    def Read_DataFrameToClassObjects(DataFrame):
        return [(C1_Fuschia_D2L1_MyWork_Entity2_List_Table(
            row.Entity1_ID,
            row.Entity2Category_ID,
            row.Entity2_Name,
            row.Entity2_Desc,
            row.Entity2_Name_Unique,
            row.Entity2_ID,
            row.Record_DateTime,
            row.Upgrade_DateTime
        )) for index, row in DataFrame.iterrows() ]
# endregion
# endregion
