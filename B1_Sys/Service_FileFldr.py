# region Import
# from ast import Pass
# from distutils.dir_util import copy_tree
# from distutils.log import error
# from msilib.schema import Error
# from pyclbr import Function
# ---
import os
import shutil
# import sys
# endregion 
# ---
FileFldr_Expt_Fldr_In_Path = "S:/Sahu_Group/C3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/A1_In"
FileFldr_Expt_File_In_Name_100 = "Default.xlsx"

FileFldr_Expt_Fldr_In_Test100_Path = FileFldr_Expt_Fldr_In_Path + "/" + "A1_Test100"
FileFldr_Expt_Fldr_In_Test101_Path = FileFldr_Expt_Fldr_In_Path + "/" + "A1_Test101"

FileFldr_Expt_Fldr_Out_Path = "S:/Sahu_Group/C3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out"
FileFldr_Expt_File_Out_Name_100 = "Default.xlsx"

FileFldr_Expt_Out_Fldr_Test100_Path = FileFldr_Expt_Fldr_Out_Path + "/" + "A1_Test100"
FileFldr_Expt_Out_Fldr_Test101_Path = FileFldr_Expt_Fldr_Out_Path + "/" + "A1_Test101"
# ---
def Create_FileFldr_List_FromPathAndNameExtension(Path_Src,NameExtensionFileFldr_List):
    for i in range(0,len(NameExtensionFileFldr_List)):
        # --
        Path_FileFldr = Path_Src+"/"+str(NameExtensionFileFldr_List[i])
        # --
        IsFileFldr = "File"
        if NameExtensionFileFldr_List[i].find(".")!=-1:
            IsFileFldr = "File"
        else:
            IsFileFldr = "Fldr"
        # --
        if IsFileFldr == "Fldr":
            if os.path.isdir(Path_FileFldr)==True:
                print("FldrPresent:Create_FileFldr_List_FromPathAndNameExtension-FileFldr:"+Path_FileFldr)
            else: 
                try:
                    os.makedirs(Path_FileFldr)
                    print("Success:Create_FileFldr_List_FromPathAndNameExtension-FileFldr:"+Path_FileFldr)
                except:
                    print("Error:Create_FileFldr_List_FromPathAndNameExtension-File:"+Path_FileFldr)
        if IsFileFldr == "File":
            if os.path.isfile(Path_FileFldr)==True:
                print("FilePresent:Create_FileFldr_List_FromPathAndNameExtension-FileFldr:"+Path_FileFldr)
            else: 
                try:
                    with open(Path_FileFldr,'w') as fp:
                        pass
                    print("Success:Create_FileFldr_List_FromPathAndNameExtension-FileFldr:"+Path_FileFldr)
                except:
                    print("Error:Create_FileFldr_List_FromPathAndNameExtension-File:"+Path_FileFldr)
# ---
def Read_FileFldr_NameExtensionPath_List_FromPath(Path_Src,Option_FileOrFldr,Option_PathOrName,Option_Filter_Name_List,Option_Filter_Extension_List):
    Result_List = []
    for EntityNameExtension in os.listdir(Path_Src):
        # --
        IsFileFldrPass = 0 
        if Option_FileOrFldr == "File" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==False:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "Fldr" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==True:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "FileFldr":
            IsFileFldrPass = 1
        # --           
        IsNamePass = 0
        if len(Option_Filter_Name_List)>0:
            for i in range(0,len(Option_Filter_Name_List)):
                if EntityNameExtension.find(str(Option_Filter_Name_List[i]))!=-1:
                    IsNamePass = IsNamePass + 1
        IsExtensionPass = 0
        if len(Option_Filter_Extension_List)>0:
            for i in range(0,len(Option_Filter_Extension_List)):
                if EntityNameExtension.endswith("."+Option_Filter_Extension_List[i]):
                    IsExtensionPass = IsExtensionPass + 1
        # --
        if IsFileFldrPass == 1 and IsNamePass == len(Option_Filter_Name_List) and IsExtensionPass == len(Option_Filter_Extension_List):
            if Option_PathOrName == "Name":
                Result_List.append(os.path.splitext(EntityNameExtension)[0])
            if Option_PathOrName == "NameExtension":
                Result_List.append(EntityNameExtension)
            if Option_PathOrName == "Path":
                Result_List.append(Path_Src+"/"+EntityNameExtension)
       
    return Result_List

def ReadWithSameNameExt_FileFldr_NameExtensionPath_List_FromPath(Path_Src,Option_FileOrFldr,Option_PathOrName,Option_Filter_Name_List,Option_Filter_Extension_List):
    Result_List = []
    for EntityNameExtension in os.listdir(Path_Src):
        # --
        IsFileFldrPass = 0 
        if Option_FileOrFldr == "File" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==False:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "Fldr" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==True:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "FileFldr":
            IsFileFldrPass = 1
        # --           
        IsNamePass = 0
        if len(Option_Filter_Name_List)>0:
            for i in range(0,len(Option_Filter_Name_List)):
                if EntityNameExtension.startswith(str(Option_Filter_Name_List[i]))==True:
                    IsNamePass = IsNamePass + 1
        IsExtensionPass = 0
        if len(Option_Filter_Extension_List)>0:
            for i in range(0,len(Option_Filter_Extension_List)):
                if EntityNameExtension.endswith("."+Option_Filter_Extension_List[i]):
                    IsExtensionPass = IsExtensionPass + 1
        # --
        if IsFileFldrPass == 1 and IsNamePass == len(Option_Filter_Name_List) and IsExtensionPass == len(Option_Filter_Extension_List):
            if Option_PathOrName == "NameExtension":
                Result_List.append(EntityNameExtension)
            if Option_PathOrName == "Path":
                Result_List.append(Path_Src+"/"+EntityNameExtension)
       
    return Result_List
# ---
def Update_RePlace_FileFldr_List_FromPath(Path_Src,Option_FileOrFldr,Option_Filter_Name_List,Option_Replace_Dict):
    Result_List = []
    for EntityNameExtension in os.listdir(Path_Src):
        # --
        IsFileFldrPass = 0 
        if Option_FileOrFldr == "File" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==False:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "Fldr" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==True:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "FileFldr":
            IsFileFldrPass = 1
        # --           
        IsNamePass = 0
        if len(Option_Filter_Name_List)>0:
            for i in range(0,len(Option_Filter_Name_List)):
                if EntityNameExtension.find(str(Option_Filter_Name_List[i]))!=-1:
                    IsNamePass = IsNamePass + 1
        # --           
        IsReplaceDictPass = 0
        if len(Option_Replace_Dict)>0:
            for i in range(0,len(Option_Replace_Dict)):
                if EntityNameExtension.find(Option_Replace_Dict[i][0])!=-1:
                    IsReplaceDictPass = IsReplaceDictPass + 1
        # --
        if IsFileFldrPass == 1 and IsNamePass == len(Option_Filter_Name_List) and IsReplaceDictPass == len(Option_Replace_Dict):
            File_Name_Src = Path_Src+"/"+EntityNameExtension
            File_Name_Dst = ""
            for EachRow in range(0,len(Option_Replace_Dict)):                
                File_Name_Dst = File_Name_Src.replace(Option_Replace_Dict[EachRow][0],Option_Replace_Dict[EachRow][1])
            try:
                os.rename(File_Name_Src,File_Name_Dst)
                print("Success-xxx:Update_RePlace_FileFldr_List_FromPath-File,Rename,Success:"+File_Name_Dst)
            except:
                print("Error-xxx:Update_RePlace_FileFldr_List_FromPath-File,Rename,Fail:"+File_Name_Src)
# ---
def UpdateMove_FileFldr_FromPathSrcPathDst(Path_Src,Path_Dst):
    try:
        shutil.move(Path_Src,Path_Dst)
        print("Success:UpdateMove_FileFldr_FromPathSrcPathDst:From-"+Path_Src+"/To-"+Path_Dst)
    except Exception as e:
        print("Error:UpdateMove_FileFldr_FromPathSrcPathDst")
        print(e)

def UpdateCopy_FileFldr_FromPathSrcPathDst(Path_Src,Path_Dst):
    try:
        if os.path.isfile(Path_Src):
            shutil.copy(Path_Src,Path_Dst)
        if os.path.isdir(Path_Src):  
            Src_Fldr_Name = os.path.basename(Path_Src)                      
            # if os.path.exists(Src_Fldr_Name)==False:
            #     os.mkdir(Path_Dst+"/"+Src_Fldr_Name)
            shutil.copytree(Path_Src,Path_Dst+"/"+Src_Fldr_Name)
        #copy_tree(Path_Src,Path_Dst)
        #shutil.copytree(Path_Src,Path_Dst)        
        print("Success:UpdateCopy_FileFldr_FromPathSrcPathDst:From-"+Path_Src+"/To-"+Path_Dst)
    except Exception as e:
        print("Error:UpdateCopy_FileFldr_FromPathSrcPathDst")
        print(e)
# ---
def Update_FileFldr_AppendZpend_FromPath(Path_Src,Option_FileOrFldr,Option_Filter_Name_List,Option_AppendZppend,AppendZppend_Name):
    Result_List = []
    for EntityNameExtension in os.listdir(Path_Src):
        # --
        IsFileFldrPass = 0 
        if Option_FileOrFldr == "File" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==False:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "Fldr" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==True:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "FileFldr":
            IsFileFldrPass = 1
        # --           
        IsNamePass = 0
        if len(Option_Filter_Name_List)>0:
            for i in range(0,len(Option_Filter_Name_List)):
                if EntityNameExtension.find(str(Option_Filter_Name_List[i]))!=-1:
                    IsNamePass = IsNamePass + 1
        # --           
        if IsFileFldrPass == 1 and IsNamePass == len(Option_Filter_Name_List):
            File_Name_Src = Path_Src+"/"+EntityNameExtension
            File_Name_Dst = ""

            if Option_AppendZppend=="Append" and Option_FileOrFldr=="Fldr":                
                File_Name_Dst = Path_Src+"/"+AppendZppend_Name+EntityNameExtension
            if Option_AppendZppend=="Zppend" and Option_FileOrFldr=="Fldr":                
                File_Name_Dst = Path_Src+"/"+EntityNameExtension+AppendZppend_Name
            if Option_AppendZppend=="Append" and Option_FileOrFldr=="File":       
                File_Name_Dst = Path_Src+"/"+AppendZppend_Name+EntityNameExtension
            if Option_AppendZppend=="Zppend" and Option_FileOrFldr=="File":                
                EntityName = EntityNameExtension.split('.')[0] 
                EntityExtension = EntityNameExtension.split('.')[1]         
                File_Name_Dst = Path_Src+"/"+EntityName+AppendZppend_Name+"."+EntityExtension

            try:
                os.rename(File_Name_Src,File_Name_Dst)
                print("Success-xxx:Update_RePlace_FileFldr_List_FromPath-File,Rename,Success:"+File_Name_Dst)
            except:
                print("Error-xxx:Update_RePlace_FileFldr_List_FromPath-File,Rename,Fail:"+File_Name_Src)
# ---
def Update_Delete_FileFldr_List_FromPath(Path_Src,Option_FileOrFldr,Option_Filter_Name_List):
    Result_List = []
    Function_Message = ""
    for EntityNameExtension in os.listdir(Path_Src):
        # --
        IsFileFldrPass = 0 
        if Option_FileOrFldr == "File" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==False:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "Fldr" and os.path.isdir(Path_Src+"/"+EntityNameExtension)==True:
            IsFileFldrPass = 1
        if Option_FileOrFldr == "FileFldr":
            IsFileFldrPass = 1

        
        # --           
        IsNamePass = 0
        if len(Option_Filter_Name_List)>0:
            for i in range(0,len(Option_Filter_Name_List)):
                if EntityNameExtension.find(str(Option_Filter_Name_List[i]))!=-1:
                    IsNamePass = IsNamePass + 1
        # --
        File_Name_Src =""
        if IsFileFldrPass == 1 and IsNamePass == len(Option_Filter_Name_List):
            File_Name_Src = Path_Src+"/"+EntityNameExtension
            try:
                if Option_FileOrFldr=="Fldr":
                    os.rmdir(File_Name_Src)
                else:
                    os.remove(File_Name_Src)
                print("Success-xxx:Delete_RePlace_FileFldr_List_From:"+File_Name_Src)
                Function_Message ="Success:Delete_RePlace_FileFldr_List_FromPath"+File_Name_Src
                return Function_Message
            except OSError as e:
                print("Failure:Delete_RePlace_FileFldr_List_FromPath:FolderNotPresent"+File_Name_Src)  
                Function_Message ="Failure:Delete_RePlace_FileFldr_List_FromPath:FolderNotPresent"+File_Name_Src
                return Function_Message
                # print(e)                
# ---
def Update_File_Content_Str_Whole(File_Path,File_Content):
    Function_Message = ""
    try:
        file1 = open(File_Path, 'w')
        # ---    
        file1.writelines(File_Content)
        # ---    
        file1.close()
        Function_Message = "Success:File:Write:"+File_Path
        print(Function_Message)
        return Function_Message
    except Exception as e:
        print(e)
# ---
# print(Read_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test100_Path,"FileFldr","NameExtension",[],[]))
# print(Read_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test100_Path,"FileFldr","NameExtension",[],['txt']))
# print(Read_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test100_Path,"FileFldr","Path",[],[]))
# print(Read_FileFldr_NameExtensionPath_List_FromPath(FileFldr_Expt_Fldr_In_Test100_Path,"File","Path",["MyWork"],["xlsx"]))

# print(Read_FileFldr_NameExtensionPath_List_FromPath("S:\Sahu_Group\B3_Data\D2_Raw_FldrFile\C1_Fuschia","Fldr","Name",["Body"],[]))
# for x in Read_FileFldr_NameExtensionPath_List_FromPath("S:\Sahu_Group\B3_Data\D2_Raw_FldrFile\C1_Fuschia","Fldr","Name",["Body"],[]):
#     print(x)
# Update_RePlace_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test101_Path,"File",[],[["aaa","bbb"]])
# Update_RePlace_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test101_Path,"File",["my"],[["dd","gg"]])
# Update_RePlace_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test101_Path,"Fldr",[],[["loda","ola"]])

# Update_RePlace_FileFldr_List_FromPath("S:/Sahu_Group/C3_Data/B2_Xcipt_Excel/CX_XXX","File",[],[["Marketing","WorkMarketing"]])
# Update_RePlace_FileFldr_List_FromPath(FileFldr_Expt_Fldr_In_Test100_Path,"Fldr",[],[["cc","dd"]])

# Create_FileFldr_List_FromPathAndNameExtension(FileFldr_Expt_Out_Fldr_Test100_Path,["aaa","abnc","aa.txt"])
# Update_Delete_FileFldr_List_FromPath("S:/Sahu_Group/C3_Data/D2_Raw_FldrFile/C1_Fuschia/D2L1_MyWork/G11_Folder/100000000_Me","Fldr",["D2L1_MyWrk_S1101_Prexxx_Root-SSVM4"])

# Update_File_Content_Str_Whole("S:/Sahu_Group/C3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/A1_In/A1_Test102/aaa.txt",'aaaa')

# UpdateMove_FileFldr_FromPathSrcPathDst("S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/aa/Folder1","S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/bb/Folder2")
#UpdateMove_FileFldr_FromPathSrcPathDst("S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/aa/Folder1","S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/bb/Folder2")
# UpdateCopy_FileFldr_FromPathSrcPathDst("S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/aa","S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/bb/Folder2")
# UpdateCopy_FileFldr_FromPathSrcPathDst("S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/f","S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C4_RschngCopn/D1_MyProduction_IT/MyDevSyb/D2_Prjct_Atmn_FileFldr/C1_Out/C1_Test102/dd")

# Update_RePlace_FileFldr_List_FromPath("S:/Sahu_Group/B3_Data/D2_Raw_FldrFile/C1_Fuschia/D3L3_MyPolicy/G11_Folder/100000000/A2_Word","File",[],[["C1_Fuschia_",""]])
