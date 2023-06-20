from datatypes import Project, Outcome
from high_water_mark import high_water_mark

beyond_the_pale_low = Outcome(
    probability=0.23, 
    oil =[0.0, 6393.0, 18362.0, 39398.0, 44571.0, 50410.0, 
          48173.0, 42497.0, 45233.0, 42034.0, 39156.0, 36749.0,
            32101.0, 38211.0, 34621.0, 35182.0, 34400.0, 29223.0, 
            26367.0, 28618.0, 25351.0, 26081.0, 25053.0, 24131.0, 
            22785.0, 25701.0, 24530.0, 21002.0, 21454.0, 20410.0,
              19754.0, 16989.0, 17711.0, 18439.0, 16372.0, 17003.0], 

    gas = [0.0, 368026.0, 932146.0, 2037912.0, 2604826.0, 2621108.0, 2344434.0, 
           2552870.0, 2387300.0, 2348036.0, 2098746.0, 1898933.0, 1963152.0, 
           1949083.0, 1934257.0, 1695750.0, 1798733.0, 1553562.0, 1705561.0, 
           1493243.0, 1493874.0, 1395934.0, 1375453.0, 1534823.0, 1245915.0, 
           1253702.0, 1184777.0, 1108226.0, 1183426.0, 1154182.0, 1150335.0, 
           1024011.0, 991156.0, 883618.0, 994024.0, 823832.0], 

    capex = [5000.0, 10000.0, 10000.0, 5000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 

    opex = [0.0, 100.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 
            300.0, 300.0, 400.0, 300.0, 300.0, 300.0, 300.0, 400.0, 300.0, 300.0,
              300.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 150.0, 
              150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0],

    leads_to= [])

beyond_the_pale_likely= Outcome(
    probability=0.62, 
    oil = [0.0, 9133.0, 24212.0, 46433.0, 56131.0, 54913.0, 54204.0, 54013.0, 
           51792.0, 51610.0, 47481.0, 46412.0, 46740.0, 42630.0, 44171.0, 41101.0,
             38979.0, 37319.0, 32378.0, 32603.0, 31557.0, 30242.0, 28956.0, 
             30055.0, 29955.0, 28715.0, 28336.0, 26900.0, 25758.0, 25436.0, 
             25846.0, 22634.0, 22830.0, 21835.0, 22247.0, 20475.0], 

    gas = [0.0, 452120.0, 1210578.0, 2345123.0, 2923487.0, 2801675.0, 2631240.0, 
           2572037.0, 2514166.0, 2529880.0, 2472958.0, 2417316.0, 2247097.0, 
           2110399.0, 2123589.0, 2014755.0, 1892191.0, 1777083.0, 1668977.0, 
           1663414.0, 1610046.0, 1512102.0, 1492571.0, 1458988.0, 1440143.0, 
           1421541.0, 1362310.0, 1318603.0, 1314208.0, 1246855.0, 1230750.0, 
           1191263.0, 1153043.0, 1149200.0, 1101317.0, 1055429.0], 

    capex = [5000.0, 10000.0, 10000.0, 5000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 

    opex =  [0.0, 100.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 
             300.0, 300.0, 400.0, 300.0, 300.0, 300.0, 300.0, 400.0, 300.0, 300.0, 
             300.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 150.0, 150.0,
               150.0, 150.0, 150.0, 150.0, 150.0, 150.0], 

    leads_to= [high_water_mark])

beyond_the_pale_high = Outcome(
    probability=0.15, 
    oil = [0.0, 10777.0, 27427.0, 59590.0, 69181.0, 72586.0, 58278.0, 58777.0, 
           62637.0, 58511.0, 58347.0, 54725.0, 53024.0, 48691.0, 48698.0, 45627.0, 
           46916.0, 44342.0, 45972.0, 45433.0, 48591.0, 45126.0, 42556.0, 36672.0,
             40169.0, 34449.0, 35922.0, 32163.0, 29546.0, 28077.0, 25917.0, 
             25001.0, 28155.0, 22089.0, 25161.0, 25042.0], 

    gas = [0.0, 560629.0, 1392165.0, 2649989.0, 3742063.0, 3277960.0, 3532842.0, 
           3004033.0, 3216522.0, 2699837.0, 2649814.0, 2758319.0, 2949582.0, 
           2488785.0, 2561340.0, 2355858.0, 2202316.0, 2314137.0, 2462791.0, 
           2497851.0, 2407157.0, 1997847.0, 1958606.0, 1795765.0, 1770624.0,
           1656182.0, 1684550.0, 1515599.0, 1573232.0, 1571099.0, 1520114.0, 
             1390463.0, 1430896.0, 1204455.0, 1300209.0, 1283415.0], 

    capex = [5000.0, 10000.0, 10000.0, 5000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 

    opex =  [0.0, 100.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 
             300.0, 500.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0,
            300.0, 250.0, 250.0, 250.0, 250.0, 450.0, 250.0, 250.0, 150.0, 
            150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0], 

    leads_to= [high_water_mark])


beyond_the_pale = Project(
    name = 'BEYOND THE PALE',
    oil_shrink=0.05,
    gas_shrink=0.1, 
    wi=0.8,
    nri=0.6,
    tax_rate=0.25,
    outcomes=[beyond_the_pale_low, beyond_the_pale_likely, beyond_the_pale_high]
)