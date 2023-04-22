from xml.etree import ElementTree as ET
import csv
tree = ET.parse("DLTINS_20210117_01of01.xml")
root = tree.getroot()

csvfile = open("extracted_data.csv", 'w', encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

csvfile_writer.writerow(["Id","FullNm","ClssfctnTp","NtnlCcy","CmmdtyDerivInd","Issr"])
for fin in root.findall(".//FinInstrmRptgRefDataDltaRpt/FinInstrm/TermntdRcrd"):

    if (fin):
        Id = fin.find("./FinInstrmGnlAttrbts/Id")
        FullNm = fin.find("./FinInstrmGnlAttrbts/FullNm")
        ClssfctnTp = fin.find("./FinInstrmGnlAttrbts/ClssfctnTp")
        NtnlCcy = fin.find("./FinInstrmGnlAttrbts/NtnlCcy")
        CmmdtyDerivInd = fin.find("./FinInstrmGnlAttrbts/CmmdtyDerivInd")
        Issr =  fin.find("Issr")
        
        csv_line = [Id.text,FullNm.text,ClssfctnTp.text,NtnlCcy.text,CmmdtyDerivInd.text,Issr.text]
        csvfile_writer.writerow(csv_line)
csvfile.close()