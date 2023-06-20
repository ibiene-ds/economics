from datatypes import Project, Outcome
from needs_more_bats import needs_more_bats
from bat_classic import bat_classic

bat_country_low = Outcome(
    probability=0.2, 
    oil = [
        0.0,
        15000.0,
        32000.0,
        61000.0,
        76000.0,
        71920.0,
        67702.0,
        63706.0,
        60168.0,
        57171.0,
        54034.0,
        51578.0,
        48679.0,
        45790.0,
        43519.0,
        41537.0,
        39361.0,
        37764.0,
        36089.0,
        34388.0,
        32636.0,
        31028.0,
        29206.0,
        27607.0,
        26173.0,
        24763.0,
        23674.0,
        22466.0,
        21397.0,
        20342.0,
        19327.0,
        18289.0,
        17304.0,
        16508.0,
        15798.0,
        14881.0,
    ], 

    gas =[
        0.0,
        6005.0,
        12829.0,
        24305.0,
        30511.0,
        28830.0,
        26948.0,
        25388.0,
        23976.0,
        22873.0,
        21643.0,
        20540.0,
        19494.0,
        18234.0,
        17484.0,
        16552.0,
        15711.0,
        15055.0,
        14455.0,
        13766.0,
        13026.0,
        12389.0,
        11708.0,
        11091.0,
        10499.0,
        9866.0,
        9431.0,
        8997.0,
        8536.0,
        8133.0,
        7739.0,
        7287.0,
        6940.0,
        6604.0,
        6324.0,
        5925.0,
    ], 
                          
    capex = [
        5000.0,
        10000.0,
        10000.0,
        5000.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        500.0,
        0.0,
        0.0,
        0.0,
        0.0,
        500.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ], 
                          
                          
    opex = [
        0.0,
        100.0,
        300.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        700.0,
        500.0,
        500.0,
        500.0,
        500.0,
        700.0,
        500.0,
        500.0,
        500.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
],                       
    leads_to=[])


bat_country_likely = Outcome(
    probability=0.6, 

    oil =[
        0.0,
        22500.0,
        48000.0,
        91500.0,
        114000.0,
        107880.0,
        101553.0,
        95559.0,
        90252.0,
        85757.0,
        81051.0,
        77367.0,
        73019.0,
        68685.0,
        65279.0,
        62306.0,
        59042.0,
        56646.0,
        54134.0,
        51582.0,
        48954.0,
        46542.0,
        43809.0,
        41411.0,
        39260.0,
        37145.0,
        35511.0,
        33699.0,
        32096.0,
        30513.0,
        28991.0,
        27434.0,
        25956.0,
        24762.0,
        23697.0,
        22322.0,
    ], 

    gas =[
        0.0,
        9008.0,
        19244.0,
        36458.0,
        45767.0,
        43245.0,
        40422.0,
        38082.0,
        35964.0,
        34310.0,
        32465.0,
        30810.0,
        29241.0,
        27351.0,
        26226.0,
        24828.0,
        23567.0,
        22583.0,
        21683.0,
        20649.0,
        19539.0,
        18584.0,
        17562.0,
        16637.0,
        15749.0,
        14799.0,
        14147.0,
        13496.0,
        12804.0,
        12200.0,
        11609.0,
        10931.0,
        10410.0,
        9906.0,
        9486.0,
        8888.0,
], 
                                             
    capex = [
        5000.0,
        10000.0,
        10000.0,
        5000.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        500.0,
        0.0,
        0.0,
        0.0,
        0.0,
        500.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
], 
                                          
    opex = [
        0.0,
        100.0,
        300.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        700.0,
        500.0,
        500.0,
        500.0,
        500.0,
        700.0,
        500.0,
        500.0,
        500.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
    ], 
                          
    leads_to=[needs_more_bats])


bat_country_high = Outcome(
    probability=0.2, 

    oil =[
        0.0,
        31500.0,
        67200.0,
        128100.0,
        159600.0,
        151032.0,
        142174.0,
        133783.0,
        126353.0,
        120059.0,
        113471.0,
        108314.0,
        102226.0,
        96159.0,
        91390.0,
        87228.0,
        82658.0,
        79304.0,
        75787.0,
        72215.0,
        68536.0,
        65159.0,
        61333.0,
        57975.0,
        54963.0,
        52002.0,
        49715.0,
        47179.0,
        44934.0,
        42718.0,
        40587.0,
        38407.0,
        36338.0,
        34667.0,
        33176.0,
        31250.0,
    ], 

    gas =[
        0.0,
        12611.0,
        26941.0,
        51041.0,
        64073.0,
        60543.0,
        56591.0,
        53315.0,
        50350.0,
        48033.0,
        45450.0,
        43134.0,
        40937.0,
        38291.0,
        36716.0,
        34759.0,
        32993.0,
        31616.0,
        30356.0,
        28909.0,
        27355.0,
        26017.0,
        24587.0,
        23291.0,
        22048.0,
        20719.0,
        19805.0,
        18894.0,
        17926.0,
        17079.0,
        16252.0,
        15303.0,
        14574.0,
        13868.0,
        13280.0,
        12443.0,
    ], 
                                                 
    capex = [
        5000.0,
        10000.0,
        10000.0,
        5000.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
], 
                                           
    opex = [
        0.0,
        100.0,
        300.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        500.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        400.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
        100.0,
], 
                          
    leads_to=[needs_more_bats, bat_classic])


bat_country = Project(
    name = 'BAT COUNTRY',
    oil_shrink=0.05,
    gas_shrink=0.1, 
    wi=0.75,
    nri=0.6,
    tax_rate=0.25,
    outcomes=[bat_country_low, bat_country_likely, bat_country_high]
)