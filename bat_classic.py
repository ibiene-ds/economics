from datatypes import Project, Outcome

bat_classic_low = Outcome(
    probability=0.55, 

    oil =[0.0, 15788.0, 19825.0, 62676.0, 47458.0, 53431.0, 57858.0, 
          54671.0, 72477.0, 46230.0, 37687.0, 47330.0, 46059.0, 32499.0, 
          39944.0, 31876.0, 37169.0, 24435.0, 27619.0, 32194.0, 30570.0, 
          27712.0, 19757.0, 25542.0, 27538.0, 23611.0, 26700.0, 20366.0,
            18437.0, 17401.0, 16417.0, 15128.0, 13553.0, 20108.0, 13206.0, 
            14703.0], 

    gas =  [0.0, 4606.0, 8044.0, 20196.0, 32609.0, 18833.0, 21545.0, 
            21983.0, 18744.0, 21581.0, 16169.0, 21593.0, 15147.0, 12717.0, 
            14348.0, 12461.0, 19525.0, 12736.0, 11186.0, 12032.0, 10841.0, 
            14301.0, 10198.0, 8747.0, 10031.0, 9761.0, 9358.0, 7555.0, 
            6160.0, 7220.0, 6272.0, 4764.0, 5385.0, 6514.0, 4933.0, 4104.0],
 
    capex= [5000.0, 9000.0, 9000.0, 2000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
            0.0, 0.0, 300.0, 0.0, 300.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
            300.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

    opex=[0.0, 100.0, 300.0, 500.0, 500.0, 500.0, 500.0, 500.0, 500.0, 
          500.0, 500.0, 500.0, 500.0, 700.0, 500.0, 700.0, 500.0, 700.0,
            500.0, 500.0, 500.0, 400.0, 400.0, 700.0, 400.0, 400.0, 400.0,
              200.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], 

    leads_to=[])


bat_classic_high = Outcome(
    probability=0.45, 

    oil = [0.0, 36288.0, 74538.0, 135812.0, 149912.0, 147286.0, 
           163955.0, 125221.0, 131357.0, 148969.0, 109273.0, 139942.0, 
           126842.0, 98005.0, 94342.0, 109515.0, 97627.0, 96909.0, 90922.0,
             65109.0, 80187.0, 79087.0, 77022.0, 51175.0, 54826.0, 62194.0, 
             64267.0, 48854.0, 52654.0, 52671.0, 44341.0, 33933.0, 40553.0,
               31824.0, 31096.0, 36281.0], 

    gas =  [0.0, 14699.0, 25850.0, 48974.0, 71916.0, 72409.0, 56387.0, 
            50521.0, 48175.0, 54498.0, 40978.0, 36880.0, 37998.0, 40014.0, 
            32428.0, 35176.0, 36596.0, 32691.0, 27900.0, 32358.0, 27971.0, 
            28723.0, 28098.0, 27586.0, 23124.0, 25903.0, 20665.0, 20632.0, 
            21934.0, 15738.0, 16021.0, 14943.0, 14796.0, 16556.0, 14462.0, 
            12648.0],

    capex=  [5000.0, 9000.0, 9000.0, 2000.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 0.0, 500.0, 0.0, 0.0, 0.0, 0.0, 300.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0], 

    opex=  [0.0, 100.0, 300.0, 600.0, 600.0, 600.0, 600.0, 600.0, 600.0, 
            500.0, 500.0, 500.0, 500.0, 700.0, 500.0, 700.0, 500.0, 700.0, 
            500.0, 500.0, 500.0, 400.0, 400.0, 700.0, 400.0, 400.0,
      400.0, 200.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], 

    leads_to=[])



bat_classic  = Project(
    name = 'BAT CLASSIC',
    oil_shrink=0.05,
    gas_shrink=0.1, 
    wi=0.2,
    nri=0.15,
    tax_rate=0.25,
    outcomes=[bat_classic_low, bat_classic_high]
)