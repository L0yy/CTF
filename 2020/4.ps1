 ${84AOhZ}  = [tYPE]("{10}{2}{7}{4}{8}{9}{1}{5}{0}{6}{3}" -F 'Lg','HY.HAs','Ystem.SE','M','.','ha','OrITH','curITY','CrYPtogRA','P','s');  function GEt-hash{
param(
    [string] ${STRiNG} = $(throw ("{3}{0}{2}{4}{1}" -f'tring','ed',' is','s',' requir')),
     [ValidateSet("MD5", {"{1}{0}"-f '56','SHA2'})]
    [string] ${AlgOriThm}
)
${UTf8} = .("{0}{2}{1}" -f 'n','ect','ew-obj') -TypeName ("{5}{0}{4}{3}{2}{1}"-f 't','g','in','F8Encod','em.Text.UT','Sys')
${HaSHER} =  (GeT-variABle  84AoHz )."VALUE"::("{0}{1}" -f 'cre','ate').Invoke(${AlgOritHM})
${Hash} = ${HasHeR}."CoMpuTEhAsh"(${utF8}.("{1}{0}"-f'es','GetByt').Invoke(${stRINg}))

 -join ( ${hAsh} | &("{0}{1}" -f'fo','reach') {"{0:X}" -f ${_}} )
}

${suDOKu} = @(
    @(0,0,6, 0,0,0, 9,0,0),
    @(0,1,0, 6,0,2, 0,3,0),
    @(4,0,0, 0,5,0, 0,0,8),
    @(0,7,0, 0,0,0, 0,8,0),
    @(0,0,4, 0,0,0, 3,0,0),
    @(0,8,0, 0,0,0, 0,9,0),
    @(7,0,0, 0,1,0, 0,6,3),
    @(0,3,0, 4,0,8, 0,1,0),
    @(0,0,9, 0,0,0, 8,0,0)
)

${FlAg} = ("{93}{73}{21}{58}{13}{63}{26}{4}{0}{19}{57}{64}{56}{18}{47}{50}{36}{103}{33}{104}{75}{10}{30}{11}{78}{88}{34}{45}{61}{65}{80}{102}{95}{85}{23}{53}{1}{90}{39}{92}{9}{14}{41}{62}{49}{86}{35}{99}{46}{76}{6}{66}{100}{84}{70}{20}{51}{87}{67}{44}{24}{91}{68}{43}{71}{16}{98}{25}{15}{40}{101}{42}{82}{27}{8}{17}{38}{60}{5}{59}{52}{55}{7}{3}{105}{83}{37}{12}{48}{32}{54}{29}{81}{79}{97}{28}{96}{94}{89}{77}{22}{69}{2}{72}{31}{74}"-f'AEMAVABC','YwBh','wA2ADkAY','AGY','wBx','A','AMABhA','AMQBhADUAMABj','ZAA3ADcAMw','EAOQBmADgAMQA4','Mg','zADcAMg','ADAA','b1','A','ABlAGIAZ','GYAZgA0AGY','BhAG','wA5AHA','AH','g','2d1116743f0423','Bi','AMwAyAGMA','GQA','A0ADkAN','45MgB8AHMAR','AGMA','QA1A','BjADEAM','A','QBhADUAM','M','PQA9AHwAZ','B','A5A','AOQBBAFMA','NwA2ADgANgAw','UAZgBiAD
','cAZ','QBmADUAZQA','DAAOQ','ANQA1AGY','ADQAZQBhADAAYgAzADc','MAMAAyA','jADIAMQBjAGU','ADIAMAAxA','AdQBwA','YgBmAD','
A','C8','A3AGUA','G','MgAzADMA','AOA','M','B1AHUAN','U','413','MgBmA','c','AO','A5AGU','6050a53','ARw','AA0ADYA','DgA','3AD','zAGMANABh','ADkAY','DUAN','AZgAxA','QA3ADAAY','649','gBlAGYA','ADEA','DUANwAxADE','ZA','AzAD','ADMA','ZQAxAGQ','AA2ADMAMABk','AYwA3','AGIAOABlAGMA','AMABjA','AYQBlAGE','Yw','OAA2ADIAZAA4ADMAMAA','cANg','AZgA2AGIA','AD','YQA','gAxAD','7','ZQAyADU','ADk','GUA','Y','ANA','DkAZgA0AGMANwAw','MwA0ADkAZAA0ADk','2AGI','AYQBi','SQBwAGcA','gAw','AMwA2')

${suDOStr} = ""
for(${i} = 0; ${I} -lt 9; ${i}++){
    for(${j} = 0; ${J} -lt 9; ${j}++){
        ${SuDOSTr} += ${SUdOKu}[${i}][${J}]     
    }
}

$b = Get-Content .\solver.csv

for(${i} = 0; ${i} -lt $b.Count; ${i}++){
    ${SuDOSTr} =  $b[${i}]
    
    ${H} = .("{2}{0}{1}"-f't-','Hash','Ge') ${SUdoSTR} -algorithm ("{1}{0}"-f 'D5','M')
    ${KeY} = [Byte[]](${h}.("{0}{2}{1}"-f'PadRi','t','gh').Invoke(32).("{0}{2}{1}"-f'Su','ring','bst').Invoke(0,32).("{3}{0}{2}{1}"-f'ha','Array','r','ToC').Invoke())

    try
    {
      ${DeCRYPTEDTeXTsEcUResTring} = ${FLaG} | &("{0}{3}{2}{1}" -f'Convert','ureString','Sec','To-') -Key ${KEy} -ErrorAction ("{0}{1}" -f'S','top')
      # ConvertTo-SecureString   Stop
      ${CReD} = .("{3}{1}{2}{0}" -f 'ect','ew','-Obj','N') -TypeName ("{0}{3}{6}{2}{1}{7}{5}{10}{4}{8}{9}"-f'Sy','n','nageme','stem.M','ion.PSC','.Automa','a','t','r','edential','t')(("{0}{1}"-f'dumm','y'), ${dECRypteDTExtsEcuRESTriNg})
      # New-Object System.Management.Automation.PSCredential dummy 
      ${dECrYPteDTEXT} = ${Cred}.("{4}{1}{2}{3}{0}{5}" -f'entia','tNe','tworkCre','d','Ge','l').Invoke()."PaSswoRd"
      # GetNetworkCredential PaSswoRd
      .("{3}{0}{2}{1}" -f 'Ho','t','s','Write-') ${DeCRYPtEDTEXT}
    }
    catch
    {
      #${DECRyPTEDTExt} = (("{2}{0}{1}"-f'g k','ey)','(wron'))
    }

    
}