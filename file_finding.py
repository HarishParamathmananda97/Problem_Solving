
def file_finding(name: str, redemg: list):
    print(name, redemg)
    sample = 'P201.$FTXPBI1.$REDEMG.$ABC0006.I'

    

files = ['P201.$FTXPBI1.$REDEMG.$ABC0006.I', 'P201.$FTXPBI1.$REDEMG.$ABC0007.I', 'P201.$FTXPBI1.$REDEMG.$ABC00100.I', 'P201.$FTXPBI1.$REDEMG.$ABC00101.I', 'P201.$FTXPBI1.$REDEMG.$ABC00102.I', 'P201.$FTXPBI1.$REDEMG.$ABC0019.I', 'P201.$FTXPBI1.$REDEMG.$ABC0027.I', 'P201.$FTXPBI1.$REDEMG.$ABC0028.I', 'P201.$FTXPBI1.$REDEMG.$ABC0029.I', 'P201.$FTXPBI1.$REDEMG.$ABC0030.I', 'P201.$FTXPBI1.$REDEMG.$ABC0031.I', 'P201.$FTXPBI1.$REDEMG.$ABC0032.I', 'P201.$FTXPBI1.$REDEMG.$ABC0033.I', 'P201.$FTXPBI1.$REDEMG.$ABC0034.I', 'P201.$FTXPBI1.$REDEMG.$ABC0035.I', 'P201.$FTXPBI1.$REDEMG.$ABC0036.I', 'P201.$FTXPBI1.$REDEMG.$ABC0037.I', 'P201.$FTXPBI1.$REDEMG.$ABC0038.I', 'P201.$FTXPBI1.$REDEMG.$ABC0039.I', 'P201.$FTXPBI1.$REDEMG.$ABC0040.I', 'P201.$FTXPBI1.$REDEMG.$ABC0041.I', 'P201.$FTXPBI1.$REDEMG.$ABC0042.I', 'P201.$FTXPBI1.$REDEMG.$ABC0043.I', 'P201.$FTXPBI1.$REDEMG.$ABC0044.I', 'P201.$FTXPBI1.$REDEMG.$ABC0045.I', 'P201.$FTXPBI1.$REDEMG.$ABC0046.I', 'P201.$FTXPBI1.$REDEMG.$ABC0047.I', 'P201.$FTXPBI1.$REDEMG.$ABC0048.I', 'P201.$FTXPBI1.$REDEMG.$ABC0049.I', 'P201.$FTXPBI1.$REDEMG.$ABC0050.I', 'P201.$FTXPBI1.$REDEMG.$ABC0051.I', 'P201.$FTXPBI1.$REDEMG.$ABC0052.I', 'P201.$FTXPBI1.$REDEMG.$ABC0053.I', 'P201.$FTXPBI1.$REDEMG.$ABC0054.I', 'P201.$FTXPBI1.$REDEMG.$ABC0055.I', 'P201.$FTXPBI1.$REDEMG.$ABC0056.I', 'P201.$FTXPBI1.$REDEMG.$ABC0057.I', 'P201.$FTXPBI1.$REDEMG.$ABC0058.I', 'P201.$FTXPBI1.$REDEMG.$ABC0059.I', 'P201.$FTXPBI1.$REDEMG.$ABC0060.I', 'P201.$FTXPBI1.$REDEMG.$ABC0061.I', 'P201.$FTXPBI1.$REDEMG.$ABC0062.I', 'P201.$FTXPBI1.$REDEMG.$ABC0063.I', 'P201.$FTXPBI1.$REDEMG.$ABC0064.I', 'P201.$FTXPBI1.$REDEMG.$ABC0065.I', 'P201.$FTXPBI1.$REDEMG.$ABC0066.I', 'P201.$FTXPBI1.$REDEMG.$ABC0067.I', 'P201.$FTXPBI1.$REDEMG.$ABC0068.I', 'P201.$FTXPBI1.$REDEMG.$ABC0069.I', 'P201.$FTXPBI1.$REDEMG.$ABC0070.I', 'P201.$FTXPBI1.$REDEMG.$ABC0071.I', 'P201.$FTXPBI1.$REDEMG.$ABC0072.I', 'P201.$FTXPBI1.$REDEMG.$ABC0073.I', 'P201.$FTXPBI1.$REDEMG.$ABC0074.I', 'P201.$FTXPBI1.$REDEMG.$ABC0075.I', 'P201.$FTXPBI1.$REDEMG.$ABC0076.I', 'P201.$FTXPBI1.$REDEMG.$ABC0077.I', 'P201.$FTXPBI1.$REDEMG.$ABC0078.I', 'P201.$FTXPBI1.$REDEMG.$ABC0079.I', 'P201.$FTXPBI1.$REDEMG.$ABC0080.I', 'P201.$FTXPBI1.$REDEMG.$ABC0081.I', 'P201.$FTXPBI1.$REDEMG.$ABC0082.I', 'P201.$FTXPBI1.$REDEMG.$ABC0083.I', 'P201.$FTXPBI1.$REDEMG.$ABC0084.I', 'P201.$FTXPBI1.$REDEMG.$ABC0085.I', 'P201.$FTXPBI1.$REDEMG.$ABC0086.I', 'P201.$FTXPBI1.$REDEMG.$ABC0087.I', 'P201.$FTXPBI1.$REDEMG.$ABC0088.I', 'P201.$FTXPBI1.$REDEMG.$ABC0089.I', 'P201.$FTXPBI1.$REDEMG.$ABC0090.I', 'P201.$FTXPBI1.$REDEMG.$ABC0091.I', 'P201.$FTXPBI1.$REDEMG.$ABC0092.I', 'P201.$FTXPBI1.$REDEMG.$ABC0093.I', 'P201.$FTXPBI1.$REDEMG.$ABC0094.I', 'P201.$FTXPBI1.$REDEMG.$ABC0095.I', 'P201.$FTXPBI1.$REDEMG.$ABC0096.I', 'P201.$FTXPBI1.$REDEMG.$ABC0097.I', 'P201.$FTXPBI1.$REDEMG.$ABC0098.I', 'P201.$FTXPBI1.$REDEMG.$ABC0099.I', 'P201.$FTXPBI1.$REDEMG.$ABC0100.I', 'P201.$FTXPBI1.$REDEMG.$ABC0101.I', 'P201.$FTXPBI1.$REDEMG.$ABC0102.I', 'P201.$FTXPBI1.$REDEMG.$ABC0103.I', 'P201.$FTXPBI1.$REDEMG.$ABC0104.I', 'P201.$FTXPBI1.$REDEMG.$ABC0105.I', 'P201.$FTXPBI1.$REDEMG.$ABC0106.I', 'P201.$FTXPBI1.$REDEMG.$ABC0107.I', 'P201.$FTXPBI1.$REDEMG.$ABC0108.I', 'P201.$FTXPBI1.$REDEMG.$ABC0109.I', 'P201.$FTXPBI1.$REDEMG.$ABC0110.I', 'P201.$FTXPBI1.$REDEMG.$ABC0111.I', 'P201.$FTXPBI1.$REDEMG.$ABC0112.I', 'P201.$FTXPBI1.$REDEMG.$ABC0113.I', 'P201.$FTXPBI1.$REDEMG.$ABC0114.I', 'P201.$FTXPBI1.$REDEMG.$ABC0115.I', 'P201.$FTXPBI1.$REDEMG.$ABC0116.I', 'P201.$FTXPBI1.$REDEMG.$ABC0117.I', 'P201.$FTXPBI1.$REDEMG.$ABC0118.I', 'P201.$FTXPBI1.$REDEMG.$ABC0119.I', 'P201.$FTXPBI1.$REDEMG.$ABC0120.I', 'P201.$FTXPBI1.$REDEMG.$ABC0121.I', 'P201.$FTXPBI1.$REDEMG.$ABC0122.I', 'P201.$FTXPBI1.$REDEMG.$ABC0123.I', 'P201.$FTXPBI1.$REDEMG.$ABC0124.I', 'P201.$FTXPBI1.$REDEMG.$ABC0125.I', 'P201.$FTXPBI1.$REDEMG.$ABC0126.I', 'P201.$FTXPBI1.$REDEMG.$ABC0127.I', 'P201.$FTXPBI1.$REDEMG.$ABC0128.I', 'P201.$FTXPBI1.$REDEMG.$ABC0129.I', 'P201.$FTXPBI1.$REDEMG.$ABC0130.I', 'P201.$FTXPBI1.$REDEMG.$ABC0132.I', 'P201.$FTXPBI1.$REDEMG.$ABC0133.I', 'P201.$FTXPBI1.$REDEMG.$ABC0134.I', 'P201.$FTXPBI1.$REDEMG.$ABC0135.I', 'P201.$FTXPBI1.$REDEMG.$ABC0136.I', 'P201.$FTXPBI1.$REDEMG.$ABC0137.I', 'P201.$FTXPBI1.$REDEMG.$ABC0138.I', 'P201.$FTXPBI1.$REDEMG.$ABC0139.I', 'P201.$FTXPBI1.$REDEMG.$ABC0140.I', 'P201.$FTXPBI1.$REDEMG.$ABC0141.I', 'P201.$FTXPBI1.$REDEMG.$ABC0142.I', 'P201.$FTXPBI1.$REDEMG.$ABC0143.I', 'P201.$FTXPBI1.$REDEMG.$ABC0144.I', 'P201.$FTXPBI1.$REDEMG.$ABC0145.I', 'P201.$FTXPBI1.$REDEMG.$ABC0146.I', 'P201.$FTXPBI1.$REDEMG.$ABC0147.I', 'P201.$FTXPBI1.$REDEMG.$ABC0148.I', 'P201.$FTXPBI1.$REDEMG.$ABC0149.I', 'P201.$FTXPBI1.$REDEMG.$ABC0150.I', 'P201.$FTXPBI1.$REDEMG.$ABC0151.I', 'P201.$FTXPBI1.$REDEMG.$ABC0152.I', 'P201.$FTXPBI1.$REDEMG.$ABC0153.I', 'P201.$FTXPBI1.$REDEMG.$ABC0154.I', 'P201.$FTXPBI1.$REDEMG.$ABC0155.I', 'P201.$FTXPBI1.$REDEMG.$ABC0156.I', 'P201.$FTXPBI1.$REDEMG.$ABC0157.I', 'P201.$FTXPBI1.$REDEMG.$ABC0158.I', 'P201.$FTXPBI1.$REDEMG.$ABC0159.I', 'P201.$FTXPBI1.$REDEMG.$ABC0160.I', 'P201.$FTXPBI1.$REDEMG.$ABC0161.I', 'P201.$FTXPBI1.$REDEMG.$ABC0162.I', 'P201.$FTXPBI1.$REDEMG.$ABC0163.I', 'P201.$FTXPBI1.$REDEMG.$ABC0164.I', 'P201.$FTXPBI1.$REDEMG.$ABC0165.I', 'P201.$FTXPBI1.$REDEMG.$ABC0166.I', 'P201.$FTXPBI1.$REDEMG.$ABC0167.I', 'P201.$FTXPBI1.$REDEMG.$ABC0168.I', 'P201.$FTXPBI1.$REDEMG.$ABC0169.I', 'P201.$FTXPBI1.$REDEMG.$ABC0170.I', 'P201.$FTXPBI1.$REDEMG.$ABC0171.I', 'P201.$FTXPBI1.$REDEMG.$ABC0172.I', 'P201.$FTXPBI1.$REDEMG.$ABC0173.I', 'P201.$FTXPBI1.$REDEMG.$ABC0174.I', 'P201.$FTXPBI1.$REDEMG.$ABC0175.I', 'P201.$FTXPBI1.$SPEC10.$ABC0080.I', 'P201.$FTXPBI1.$SPEC11.$ABC0078.I', 'P201.$FTXPBI1.$SPEC12.$ABC0134.I']
name = 'P201.$FTXPBI1.$REDEMG.$'
count = 0
redemg = []
for file in files:
    if name in file:
        # print(file)
        redemg.append(file)
        count += 1
    
print(count)
print(redemg)
f_name = [file.replace(name,'') for file in redemg]
