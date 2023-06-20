from datatypes import Project, Outcome


high_water_mark_low = Outcome(
    probability=0.40,
    oil =[0.0, 6576.0, 18159.0, 32967.0, 38169.0, 37341.0, 40653.0, 36189.0, 
          35736.0, 35611.0, 33237.0, 30168.0, 30381.0, 27710.0, 28711.0, 26716.0, 
          26506.0, 25377.0, 22341.0, 22822.0, 23352.0, 20262.0, 20559.0, 20738.0, 
          22167.0, 20101.0, 20969.0, 17485.0, 16743.0, 18568.0, 18868.0, 15844.0, 
          15524.0, 15285.0, 15795.0, 14742.0], 
 
    gas = [0.0, 379555.0, 974515.0, 1806917.0, 2420647.0, 2319787.0, 2178667.0, 
           2040911.0, 1937165.0, 2152928.0, 2132926.0, 1918140.0, 1860596.0,
             1820219.0, 1660647.0, 1691387.0, 1436173.0, 1450988.0, 1362720.0, 
             1434695.0, 1351634.0, 1286799.0, 1270178.0, 1107372.0, 1175877.0, 
             1193384.0, 1033993.0, 1106967.0, 1103278.0, 1075412.0, 948293.0, 
             1000065.0, 994500.0, 964753.0, 861230.0, 813208.0], 

    capex = [5000.0, 10000.0, 10000.0, 5000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                  0.0], 

    opex = [0.0, 100.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 
            300.0, 300.0, 400.0, 300.0, 300.0, 300.0, 300.0, 400.0, 300.0, 300.0,
              300.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 250.0, 150.0, 
              150.0, 200.0, 150.0, 150.0, 150.0, 150.0, 150.0], 

    leads_to= []) 


high_water_mark_high = Outcome(
    probability=0.60,
    oil =[0.0, 2831.0, 10653.0, 14859.0, 25259.0, 16474.0, 23850.0, 16744.0, 
          16056.0, 23225.0, 17093.0, 20885.0, 14489.0, 15773.0, 17668.0, 13563.0, 
          16371.0, 12315.0, 13923.0, 10759.0, 10414.0, 9375.0, 10714.0, 11120.0, 
          10484.0, 10337.0, 9351.0, 9415.0, 8500.0, 10683.0, 10080.0, 9280.0, 
          7306.0, 7861.0, 7342.0, 8190.0], 

    gas = [0.0, 736956.0, 1440588.0, 2978306.0, 5057633.0, 4426647.0, 3236425.0, 
           3009283.0, 3293557.0, 3820119.0, 4327677.0, 4254476.0, 2921226.0, 
           3545470.0, 2420891.0, 2619182.0, 2176020.0, 2310208.0, 2069531.0, 
           2062633.0, 2527772.0, 2086701.0, 2522445.0, 1707016.0, 2505849.0, 
           2231819.0, 2247812.0, 1951532.0, 1537623.0, 1371541.0, 1526130.0, 
           1810720.0, 1429773.0, 1390532.0, 1431712.0, 
           1551481.0], 

    capex = [5000.0, 10000.0, 10000.0, 5000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 0.0, 250.0, 250.0, 0.0, 0.0, 
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
             0.0], 

    opex = [0.0, 100.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 300.0, 400.0, 300.0, 300.0, 300.0, 300.0, 400.0, 400.0, 400.0, 300.0, 350.0, 250.0, 350.0, 250.0, 250.0, 
            250.0, 250.0, 150.0, 150.0, 350.0, 150.0, 150.0, 150.0, 150.0, 
            150.0],

    leads_to= []) 


high_water_mark  = Project(
    name = 'HIGH WATER MARK',
    oil_shrink=0.05,
    gas_shrink=0.1, 
    wi=0.7,
    nri=0.55,
    tax_rate=0.25,
    outcomes=[high_water_mark_low, high_water_mark_high]
)