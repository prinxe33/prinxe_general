## DAILY MARKET OUTLOOK

main_etfs = [
    "SPY",  # SPDR S&P 500 ETF Trust
    "VTI",  # Vanguard Total Stock Market ETF
    "QQQ",  # Invesco QQQ Trust
    "IVV",  # iShares Core S&P 500 ETF
    "VOO",  # Vanguard S&P 500 ETF
    "IWM",  # iShares Russell 2000 ETF
    "VEA",  # Vanguard FTSE Developed Markets ETF
    "VWO",  # Vanguard FTSE Emerging Markets ETF
    "AGG",  # iShares Core U.S. Aggregate Bond ETF
    "BND",  # Vanguard Total Bond Market ETF
    "GLD",  # SPDR Gold Shares
    "IEFA", # iShares Core MSCI EAFE ETF
    "EFA",  # iShares MSCI EAFE ETF
    "EEM",  # iShares MSCI Emerging Markets ETF
    "SCHB", # Schwab U.S. Broad Market ETF
    "VTV",  # Vanguard Value ETF
    "VO",   # Vanguard Mid-Cap ETF
    "VB",   # Vanguard Small-Cap ETF
    "VEU",  # Vanguard FTSE All-World ex-US ETF
    "VIG",  # Vanguard Dividend Appreciation ETF
    "BNDX", # Vanguard Total International Bond ETF
    "VT",   # Vanguard Total World Stock ETF
    "LQD",  # iShares iBoxx $ Investment Grade Corporate Bond ETF
    "IWF",  # iShares Russell 1000 Growth ETF
    "IWD"   # iShares Russell 1000 Value ETF
    ]

international_etfs = [] 
treasury_bonds = []

energy_sector = [
    "XOM", "CVX", "PTR", "RDS-A", "TOT", "BP", "SNP", "ENB", "COP", "EQNR", 
    "KMI", "SLB", "PBR", "EOG", "PXD", "SU", "E", "WMB", "OGZPY", "RDS-B", 
    "EOCC", "EPD", "PAA", "PSX", "EOG", "ENB", "MMP", "ET", "KMI", "TRP", 
    "OKE", "MPC", "WMB", "VLO", "TRGP", "HAL", "BKR", "MPLX", "PXD", "XOM"]
 
energy_oil_materials = [] 

consumer_discretionary_sector = [
    "AMZN", "TSLA", "HD", "MCD", "NKE", "BKNG", "DIS", "LVS", "SBUX", "LOW", 
    "LULU", "EBAY", "GM", "ETSY", "EBAY", "AZO", "COST", "RACE", "ROST", "MAR", 
    "LAD", "BBY", "DKS", "SKX", "SYY", "RH", "UAA", "BWA", "LB", "ORLY", 
    "NWL", "LVS", "AZO", "KMX", "TSCO", "MAT", "APTV", "NVR", "FOXA", "DHI"]

financial_sector = [
    "JPM", "BRK-A", "BAC", "WFC", "C", "MA", "V", "GS", "AXP", "HSBC", 
    "PYPL", "UBS", "TD", "BLK", "MS", "SPGI", "SCHW", "MMC", "BABA", "AON", 
    "BMO", "PFG", "ICE", "PGR", "MSCI", "RE", "GS", "CBOE", "CME", "AMP", 
    "BX", "WFC", "COF", "TFC", "AXP", "BNS", "AIG", "DFS", "MET", "TRV"]

industrial_sector = [
    "BA", "LMT", "HON", "UNP", "CAT", "UPS", "MMM", "GE", "RTX", "DHR", 
    "FDX", "DE", "DAL", "NSC", "CSX", "EMR", "ETN", "ITW", "JCI", "ROP", 
    "EMR", "AME", "ROP", "RSG", "ITW", "SWK", "PH", "FTV", "AOS", "ROK", 
    "IR", "ALLE", "DOV", "LHX", "NVT", "WAB", "CPRT", "TXT", "ODFL", "NLSN"]

healthcare_sector = [
    "JNJ", "PFE", "UNH", "MRK", "NVS", "ABT", "TMO", "AMGN", "MDT", "BMY", 
    "ABBV", "LLY", "DHR", "GSK", "VRTX", "SNY", "BIIB", "CELG", "ZTS", "BDX", 
    "IDXX", "BIO", "HOLX", "ALGN", "CRL", "IQV", "IDXX", "CDNA", "VICI", "SGEN", 
    "MRNA", "UTHR", "ABMD", "JAZZ", "WST", "TFX", "HRC", "PKI", "PRAH", "TECH"]

consumer_staples_sector = [
    "PG", "KO", "PEP", "WMT", "COST", "PM", "NKE", "CL", "UL", "MO", 
    "EL", "KHC", "KMB", "SYY", "GIS", "MDLZ", "WBA", "STZ", "KR", "HRL", 
    "DEO", "COST", "HSY", "SYY", "ADM", "K", "EL", "TSN", "CHD", "MKC", 
    "KHC", "CL", "TAP", "CLX", "CPB", "CAG", "KR", "WMT", "GIS", "STZ"]

information_technology_sector = [
    "AAPL", "MSFT", "GOOGL", "GOOG", "TSM", "NVDA", "INTC", "ASML", "CSCO", 
    "ORCL", "SAP", "ADBE", "AVGO", "TXN", "CRM", "IBM", "QCOM", "MU", 
    "ACN", "INTU", "MXIM", "ADI", "FTNT", "SWKS", "QRVO", "WDC", "STX", 
    "APH", "ANSS", "CDNS", "LSCC", "LDOS", "MCHP", "CDW", "KEYS", "NTAP", 
    "ZBRA", "LDOS", "NTAP", "LRCX"]

telecommunication_services_sector = [
    "T", "VZ", "CHL", "TMUS", "BT", "DTEGY", "ORAN", "S", "CHA", "BCE", 
    "SKM", "TLK", "TEL", "VIV", "AMX", "CHU", "TI", "RCI", "LVLT", "NTT", 
    "VG", "VG", "VG", "VG", "VG", "VG", "VG", "VG", "VG", "VG", 
    "VG", "VG", "VG", "VG", "VG", "VG", "VG", "VG", "VG", "VG"]

utilities_sector = [
    "NEE", "DUK", "D", "SO", "EXC", "NGG", "SRE", "AEP", "XEL", "PEG", 
    "EIX", "PCG", "ED", "FE", "CNP", "AES", "AWK", "WM", "ES", "OKE", 
    "AES", "ATO", "AVA", "BKH", "CNP", "CMS", "CNL", "CPK", "CWT", "D", 
    "DGAS", "DTE", "ED", "EIX", "ES", "ETR", "FE", "HE", "IDA", "MGEE"]

materials_sector = [
    "LIN", "SHW", "BHP", "NEM", "APD", "RIO", "DOW", "VALE", "ECL", "CTVA", 
    "BBL", "PPG", "LYB", "GOLD", "FMC", "FCX", "MT", "EMN", "IFF", "DD", 
    "APTV", "CF", "CMA", "FCX", "IFF", "IP", "MLM", "MOS", "NUE", "PPG",     
    "SEE", "VMC", "WRK", "DD", "LYB", "CE", "ALB", "ALB", "EMN", "ECL"]

real_estate_sector = [
    "SPG", "CBRE", "PLD", "EQIX", "AVB", "CCI", "WELL", "BXP", "PSA", "DLR", 
    "ARE", "VTR", "EQR", "O", "WY", "UDR", "IRM", "AMT", "CB", "EXR", 
    "REG", "BXP", "PSA", "PLD", "AVB", "CCI", "EQIX", "WELL", "DRE", "O", 
    "UDR", "EQR", "ESS", "VTR", "ARE", "CBRE", "IRM", "WY", "HST", "SLG"]

international_etfs = [
    ["USA", "SPY", "VTI", "QQQ", "IVV", "VOO", "IWM", "VO", "VTV", "VB"],  # SPDR S&P 500 ETF Trust, Vanguard Total Stock Market ETF, Invesco QQQ Trust, iShares Core S&P 500 ETF, Vanguard S&P 500 ETF, iShares Russell 2000 ETF, Vanguard Mid-Cap ETF, Vanguard Mid-Cap Growth ETF, Vanguard Value ETF, Vanguard Small-Cap ETF
    ["China", "MCHI", "FXI", "ASHR", "KWEB", "CNXT", "PEK", "CHIQ", "PGJ", "CHIL"],  # iShares MSCI China ETF, iShares China Large-Cap ETF, Xtrackers Harvest CSI 300 China A-Shares ETF, KraneShares CSI China Internet ETF, VanEck Vectors ChinaAMC SME-ChiNext ETF, VanEck Vectors ChinaAMC CSI 300 ETF, Global X MSCI China Consumer Discretionary ETF, Invesco Golden Dragon China ETF, Global X MSCI China Real Estate ETF, Global X MSCI China Large-Cap 50 ETF
    ["Japan", "EWJ", "DXJ", "HEWJ", "DBJP", "EWV", "JPNL", "FLJP", "FJP", "SCJ"],  # iShares MSCI Japan ETF, WisdomTree Japan Hedged Equity Fund, iShares Currency Hedged MSCI Japan ETF, Xtrackers MSCI Japan Hedged Equity ETF, WisdomTree Japan SmallCap Dividend Fund, Direxion Daily Japan Bull 3x Shares, Franklin FTSE Japan ETF, First Trust Japan AlphaDEX Fund, iShares MSCI Japan Small-Cap ETF
    ["Germany", "EWG", "DBGR", "DXGE", "HEWG", "EWGS", "GRMY", "FDD", "GGOV"],  # iShares MSCI Germany ETF, Xtrackers MSCI Germany Hedged Equity ETF, WisdomTree Germany Hedged Equity Fund, iShares Currency Hedged MSCI Germany ETF, iShares MSCI Germany Small-Cap ETF, Xtrackers Germany Equity ETF, UBS AG FI Enhanced Global High Yield ETN, Global X GOAT Funds of Funds ETF
    ["India", "INDA", "EPI", "PIN", "IXN", "INDY", "INDL", "SMIN", "INCO", "SCIF"],  # iShares MSCI India ETF, WisdomTree India Earnings Fund, Invesco India ETF, iShares Global Tech ETF, iShares India 50 ETF, iShares India Infrastructure ETF, iShares MSCI India Small-Cap ETF, iShares MSCI India Value ETF, VanEck Vectors India Growth Leaders ETF, VanEck Vectors India Small-Cap Index ETF
    ["UK", "EWU", "EWGB", "FKU", "DXPS", "EWUS", "HEWU", "QGBR", "DDUK", "LDUK"],  # iShares MSCI United Kingdom ETF, iShares MSCI United Kingdom Small-Cap ETF, First Trust United Kingdom AlphaDEX Fund, WisdomTree United Kingdom Hedged Equity Fund, iShares MSCI United Kingdom ETF, iShares MSCI United Kingdom ETF, iShares MSCI United Kingdom ETF, SPDR MSCI United Kingdom StrategicFactors ETF, WisdomTree United Kingdom Hedged Equity Fund, iShares MSCI United Kingdom ETF
    ["France", "EWQ", "CACG", "FRAK", "FLFR", "FRN", "EWQY", "FDD", "FBGX", "DAX"],  # iShares MSCI France ETF, ClearBridge All Cap Growth ETF, Franklin FTSE France ETF, Franklin FTSE France ETF, Invesco Frontier Markets ETF, SPDR MSCI Germany StrategicFactors ETF, UBS AG FI Enhanced Global High Yield ETN, Global X GOAT Funds of Funds ETF, Global X DAX Germany ETF
    ["Brazil", "EWZ", "BRZU", "BRF", "BRAQ", "BRAF", "BRZS", "EWZS", "BRZU", "BRAZ"],  # iShares MSCI Brazil ETF, Direxion Daily MSCI Brazil Bull 2X Shares, VanEck Vectors Brazil Small-Cap ETF, Global X Brazil Consumer ETF, Global X Brazil Financials ETF, Direxion Daily MSCI Brazil Bull 3X Shares, iShares MSCI Brazil Small-Cap ETF, VanEck Vectors Brazil Small-Cap ETF, Direxion Daily MSCI Brazil Bull 2X Shares, Global X Brazil Mid Cap ETF
    ["Italy", "EWI", "FLIY", "DBIT", "ITLY", "HEWI", "EWIT", "IDOG"],  # iShares MSCI Italy ETF, Franklin FTSE Italy ETF, iShares iBonds Dec 2030 Term Treasury ETF, iShares Italy Government Bond ETF, iShares Currency Hedged MSCI Italy ETF, iShares MSCI Italy ETF, iShares MSCI Italy ETF, ALPS International Sector Dividend Dogs ETF
    ["Canada", "EWC", "CNDA", "FCCD", "FCAN", "DXC", "EWCS", "FCAN"],  # iShares MSCI Canada ETF, IQ Canada Small Cap ETF, First Trust Canada AlphaDEX Fund, First Trust Canada ETF, First Trust BICK Index Fund, iShares MSCI Canada Small-Cap ETF, First Trust Canada ETF
    ["South Korea", "EWY", "FLKR", "DBKO", "HKOR", "DWKO", "HEWY", "KORU", "KORP", "KORZ"],  # iShares MSCI South Korea ETF, Franklin FTSE South Korea ETF, Deutsche X-trackers MSCI South Korea Hedged Equity ETF, Horizons Korea KOSPI 200 ETF, Invesco MSCI South Korea ETF, Deutsche X-trackers MSCI South Korea Hedged Equity ETF, iShares Currency Hedged MSCI South Korea ETF, Direxion Daily South Korea Bull 3X Shares, Direxion Daily South Korea Bull 2X Shares, Direxion Daily South Korea Bull 2X Shares
    ["Russia", "RSX", "ERUS", "RBL", "RUSS", "RUSL", "RSXJ", "RUDR", "RU", "URR"],  # VanEck Vectors Russia ETF, iShares MSCI Russia ETF, SPDR S&P Russia ETF, Direxion Daily Russia Bull 2X Shares, Direxion Daily Russia Bear 3X Shares, Direxion Daily Russia Bull 2X Shares, VanEck Vectors Russia Small-Cap ETF, DBX ETF Trust - DBX RUSS 2X CE, Lysander-Slater Preferred Share ActivETF
    ["Australia", "EWA", "AUSE", "IAA", "HEWA", "FAUS", "BNKS", "MNRS", "FLAU"],  # iShares MSCI Australia ETF, WisdomTree Australia Dividend Fund, iShares Asia 50 ETF, iShares MSCI Australia ETF, First Trust Australia AlphaDEX Fund, UBS AG FI Enhanced Global High Yield ETN, Monarch Casino & Resort Inc., Minerco Inc, Franklin FTSE Australia ETF
    ["Spain", "EWP", "BUNT", "HEWP", "EZU", "DAX", "EDIV", "EMDD", "BOND"],  # iShares MSCI Spain ETF, Innovator 20+ Year Treasury Bond 5 Buffer ETF, iShares Currency Hedged MSCI Spain ETF, iShares MSCI Eurozone ETF, Global X DAX Germany ETF, SPDR S&P Emerging Markets Dividend ETF, SPDR S&P Emerging Markets Dividend ETF, PIMCO Total Return Exchange-Traded Fund
    ["Mexico", "EWW", "MEXX", "HEWW", "IMEX", "UBS", "SMK", "VWO"],  # iShares MSCI Mexico ETF, Direxion Daily MSCI Mexico Bull 3X Shares, iShares MSCI Mexico Capped ETF, VanEck Vectors Gulf States Index ETF, iShares Currency Hedged MSCI Mexico ETF, UBS AG FI Enhanced Global High Yield ETN, ProShares UltraShort MSCI Mexico Capped IMI, Vanguard FTSE Emerging Markets ETF
    ["Indonesia", "EIDO", "IDX", "EPHE", "IDXJ"],  # iShares MSCI Indonesia ETF, VanEck Vectors Indonesia Index ETF, iShares MSCI Philippines ETF, VanEck Vectors Indonesia Small-Cap ETF
    ["Netherlands", "EWN", "DBND", "HEWN", "EZU"],  # iShares MSCI Netherlands ETF, DBX ETF Trust - DBX mun, iShares Currency Hedged MSCI Netherlands ETF, iShares MSCI Eurozone ETF
    ["Saudi Arabia", "KSA", "DBSA", "SAUD", "FKSA", "AXJL", "MEAX", "STOT", "AXJS", "MESA"],  # iShares MSCI Saudi Arabia ETF, Invesco BulletShares 2028 USD Emerging Markets Debt ETF, iShares MSCI Saudi Arabia ETF, iShares MSCI Saudi Arabia ETF, Franklin FTSE Saudi Arabia ETF, WisdomTree Asia Pacific ex-Japan Fund, iShares MSCI Saudi Arabia ETF, SPDR STOXX Europe 50 ETF, iShares MSCI Saudi Arabia ETF, ETFMG Alternative Harvest ETF
    ["Turkey", "TUR", "DBKO"],  # iShares MSCI Turkey ETF, Xtrackers MSCI South Korea Hedged Equity ETF
    ["Switzerland", "EWL", "DBCH", "HEDJ", "DXFS", "EXI", "IDOG"]  # iShares MSCI Switzerland ETF, DBX ETF Trust - DBX China CSI 300, WisdomTree Europe Hedged Equity Fund, WisdomTree US SmallCap Fund, WisdomTree Europe SmallCap Dividend Fund, ALPS International Sector Dividend Dogs ETF
    ["Argentina", "ARG", "ARGT", "YPF", "TEO", "PAMP"],  # Global X MSCI Argentina ETF, YPF SA, Telecom Argentina SA, Pampa Energia SA
    ["Thailand", "THD", "KBANK", "PTT", "CPALL", "SCB"],  # iShares MSCI Thailand ETF, Kasikornbank PCL, PTT PCL, CP All PCL, Siam Commercial Bank PCL
    ["Austria", "EWO", "OMV", "VOE", "ANDR", "BWIN"],  # iShares MSCI Austria ETF, OMV AG, Voestalpine AG, Andritz AG, Bwin Interactive Entertainment AG
    ["United Arab Emirates", "UAE", "FAB", "EMAAR", "DPW", "ADNOC"],  # iShares MSCI UAE ETF, First Abu Dhabi Bank PJSC, Emaar Properties PJSC, DP World Ltd, Abu Dhabi National Oil Co
    ["Norway", "NOR", "NHY", "ORK", "DNB", "STB"]  # Global X MSCI Norway ETF, Norsk Hydro ASA, Orkla ASA, DNB ASA, Storebrand ASA
    ["Bangladesh", "BNG", "Grameenphone Limited", "Beximco Pharmaceuticals Limited", "BRAC Bank Limited", "Renata Limited"],  # Grameenphone (BNG), Beximco Pharmaceuticals (BNG), BRAC Bank (BNG), Renata (BNG)
    ["Kuwait", "KWT", "Kuwait Finance House K.S.C.P.", "National Bank of Kuwait S.A.K.P.", "Zain Group", "Kuwait Projects Company Holding K.S.C.P."],  # Kuwait Finance House (KWT), National Bank of Kuwait (KWT), Zain Group (KWT), Kuwait Projects Company (KWT)
    ["Slovakia", "SVK", "Slovenská pošta, a.s.", "Slovnaft, a.s.", "Slovenské elektrárne, a.s."],  # Slovenská pošta (SVK), Slovnaft (SVK), Slovenské elektrárne (SVK)
    ["Sri Lanka", "LKA", "John Keells Holdings PLC", "Commercial Bank of Ceylon PLC", "Dialog Axiata PLC", "Ceylon Tobacco Company PLC"],  # John Keells Holdings (LKA), Commercial Bank of Ceylon (LKA), Dialog Axiata (LKA), Ceylon Tobacco Company (LKA)
    ["Ethiopia", "ETH", "Commercial Bank of Ethiopia", "Ethiopian Airlines Group", "Ethiopian Electric Power Corporation", "Wegagen Bank"],  # Commercial Bank of Ethiopia (ETH), Ethiopian Airlines (ETH), Ethiopian Electric Power (ETH), Wegagen Bank (ETH)
    ["Syria", "SYR", "Syrian Steel Company", "Commercial Bank of Syria", "Cham Bank", "Barada TV"],  # Syrian Steel Company (SYR), Commercial Bank of Syria (SYR), Cham Bank (SYR), Barada TV (SYR)
    ["Dominican Republic", "DOM", "Banco Popular Dominicano", "Grupo Popular, S.A.", "Cervecería Nacional Dominicana", "Rica Group"],  # Banco Popular Dominicano (DOM), Grupo Popular (DOM), Cervecería Nacional Dominicana (DOM), Rica Group (DOM)
    ["Sudan", "SDN", "Bank of Sudan", "Khalifa Group", "DAL Group", "GIAD Group"],  # Bank of Sudan (SDN), Khalifa Group (SDN), DAL Group (SDN), GIAD Group (SDN)
    ["Kenya", "KEN", "Safaricom PLC", "Equity Group Holdings Limited", "Kenya Commercial Bank Group", "East African Breweries Limited"],  # Safaricom (KEN), Equity Group Holdings (KEN), Kenya Commercial Bank (KEN), East African Breweries Limited (KEN)
    ["Guatemala", "GTM", "Banco Industrial, S.A.", "Cervecería Centro Americana, S.A.", "Banco G&T Continental, S.A.", "Cementos Progreso, S.A."]  # Banco Industrial (GTM), Cervecería Centro Americana (GTM), Banco G&T Continental (GTM), Cementos Progreso (GTM)
    ["Belgium", "BEL", "Anheuser-Busch InBev SA/NV", "Solvay SA", "KBC Group NV", "UCB SA"],  # Anheuser-Busch InBev (BEL), Solvay (BEL), KBC Group (BEL), UCB (BEL)
    ["Colombia", "COL", "Ecopetrol SA", "Grupo Aval Acciones y Valores SA", "Bancolombia SA", "Almacenes Exito SA"],  # Ecopetrol (COL), Grupo Aval (COL), Bancolombia (COL), Almacenes Exito (COL)
    ["Egypt", "EGY", "Commercial International Bank (Egypt) SAE", "Talaat Moustafa Group Holding", "Global Telecom Holding SAE", "Ezz Steel Company SAE"],  # Commercial International Bank (EGY), Talaat Moustafa Group Holding (EGY), Global Telecom Holding (EGY), Ezz Steel Company (EGY)
    ["Finland", "FIN", "Neste Oyj", "Kone Oyj", "Nordea Bank Abp", "Fortum Oyj"],  # Neste (FIN), Kone (FIN), Nordea Bank (FIN), Fortum (FIN)
    ["Greece", "GRC", "National Bank of Greece SA", "Hellenic Telecommunications Organization SA", "Piraeus Bank SA", "OPAP SA"],  # National Bank of Greece (GRC), Hellenic Telecommunications Organization (GRC), Piraeus Bank (GRC), OPAP (GRC)
    ["Hungary", "HUN", "OTP Bank Nyrt", "MOL Hungarian Oil and Gas Plc", "Magyar Telekom Telecommunications Plc", "Gedeon Richter Plc"],  # OTP Bank (HUN), MOL Hungarian Oil and Gas (HUN), Magyar Telekom Telecommunications (HUN), Gedeon Richter (HUN)
    ["Ireland", "IRL", "CRH PLC", "Accenture PLC", "Kerry Group PLC", "Ryanair Holdings PLC"],  # CRH (IRL), Accenture (IRL), Kerry Group (IRL), Ryanair Holdings (IRL)
    ["Hong Kong", "HKG", "HSBC Holdings PLC", "AIA Group Ltd", "CK Hutchison Holdings Ltd", "Hong Kong Exchanges & Clearing Ltd"]  # HSBC Holdings (HKG), AIA Group (HKG), CK Hutchison Holdings (HKG), Hong Kong Exchanges & Clearing (HKG)
]

