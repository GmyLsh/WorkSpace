#!python 3
#filename: draw.py
#调用turtle库
import turtle
import time
#轮廓坐标，坐标由另一个python程序得到，这里显得比较简单粗暴
rose = [[-283, -136], [-281, -139], [-280, -141], [-279, -143], [-276, -147], [-273, -132], [-273, -149], [-273, -150], [-271, -150], [-268, -133], [-264, -134], [-264, -158], [-263, -157], [-261, -160], [-259, -159], [-256, -135], [-255, -135], [-254, -135], [-253, -164], [-250, -164], [-249, -165], [-249, -170], [-248, -136], [-248, -166], [-247, -136], [-244, -137], [-241, -170], [-237, -171], [-236, -170], [-235, -169], [-234, -169], [-233, -170], [-232, -139], [-227, -169], [-226, -175], [-223, -141], [-223, -161], [-223, -177], [-220, -179], [-219, -159], [-218, -175], [-217, -181], [-213, -157], [-213, -178], [-212, -156], [-208, 45], [-208, -186], [-207, 49], [-207, -144], [-206, 49], [-206, -152], [-206, -182], [-205, -167], [-204, -151], [-203, -147], [-203, -159], [-203, -162], [-203, -189], [-203, -193], [-202, -160], [-201, -160], [-200, -147], [-200, -182], [-200, -183], [-200, -185], [-199, 48], [-199, 42], [-198, -192], [-196, 47], [-196, -155], [-196, -187], [-196, -193], [-195, -185], [-194, 42], [-194, -153], [-194, -189], [-193, 42], [-192, 42], [-190, 42], [-189, 44], [-189, 42], [-189, -197], [-188, 42], [-188, 39], [-185, -151], [-185, -199], [-184, -151], [-182, -191], [-181, 41], [-181, -150], [-180, 41], [-179, 41], [-179, -202], [-179, -203], [-178, 41], [-177, 45], [-176, 41], [-175, -89], [-175, -199], [-175, -207], [-174, 46], [-174, -93], [-174, -94], [-174, -194], [-174, -205], [-173, -88], [-173, -95], [-172, -152], [-172, -206], [-170, -202], [-169, -203], [-167, -157], [-167, -196], [-167, -211], [-166, -196], [-165, -101], [-165, -103], [-165, -213], [-164, 36], [-164, -104], [-164, -214], [-163, 36], [-163, -104], [-163, -181], [-163, -208], [-163, -215], [-162, 48], [-162, 37], [-162, 36], [-162, -165], [-162, -216], [-161, 48], [-161, 36], [-161, -166], [-161, -183], [-161, -217], [-160, 48], [-160, 36], [-160, -106], [-160, -167], [-159, 48], [-159, -107], [-159, -180], [-158, 48], [-158, -183], [-157, -228], [-156, -86], [-156, -182], [-156, -231], [-155, -86], [-155, -181], [-155, -197], [-155, -281], [-154, 38], [-154, -86], [-154, -216], [-154, -238], [-154, -239], [-154, -240], [-154, -266], [-154, -269], [-154, -270], [-154, -271], [-154, -284], [-154, -285], [-153, -86], [-153, -177], [-153, -196], [-152, 49], [-152, -179], [-152, -180], [-152, -195], [-151, -174], [-150, 35], [-149, 35], [-149, -219], [-148, 50], [-148, 40], [-148, 35], [-148, -215], [-147, 38], [-147, 36], [-147, -209], [-146, 40], [-146, -154], [-146, -199], [-146, -200], [-145, -154], [-145, -186], [-145, -187], [-145, -189], [-144, 53], [-144, -154], [-144, -162], [-144, -163], [-144, -164], [-144, -165], [-144, -166], [-143, 54], [-143, -142], [-143, -143], [-143, -144], [-142, 41], [-142, -136], [-142, -137], [-142, -252], [-142, -253], [-142, -254], [-142, -255], [-142, -256], [-142, -300], [-141, -87], [-141, -118], [-141, -127], [-141, -128], [-141, -242], [-141, -243], [-140, 44], [-140, -87], [-140, -119], [-140, -122], [-140, -235], [-140, -236], [-140, -237], [-139, 45], [-139, -230], [-138, -87], [-137, -221], [-135, -85], [-135, -86], [-134, -77], [-134, -78], [-134, -79], [-134, -200], [-134, -214], [-133, 52], [-133, -157], [-133, -195], [-133, -213], [-132, 54], [-132, -62], [-132, -63], [-132, -64], [-132, -139], [-132, -173], [-131, -56], [-131, -132], [-131, -133], [-130, -49], [-130, -50], [-130, -125], [-130, -126], [-130, -185], [-129, -42], [-129, -125], [-129, -157], [-129, -169], [-129, -181], [-128, -35], [-128, -36], [-128, -157], [-128, -179], [-127, -30], [-127, -126], [-127, -157], [-127, -177], [-126, -23], [-126, -157], [-125, -15], [-125, -16], [-125, -91], [-125, -174], [-124, -11], [-124, -85], [-124, -86], [-124, -164], [-123, -2], [-123, -3], [-123, -128], [-123, -160], [-122, 3], [-122, -72], [-122, -73], [-122, -74], [-122, -75], [-122, -93], [-122, -129], [-122, -145], [-122, -156], [-121, 10], [-121, 9], [-121, -66], [-121, -67], [-121, -129], [-121, -130], [-120, -59], [-119, 46], [-119, 24], [-119, 23], [-119, -53], [-119, -55], [-118, 29], [-117, 39], [-117, 36], [-117, -96], [-116, -34], [-116, -35], [-116, -160], [-116, -170], [-116, -174], [-116, -178], [-116, -180], [-115, -28], [-115, -29], [-115, -136], [-115, -167], [-115, -181], [-115, -184], [-114, -22], [-114, -133], [-114, -188], [-113, -17], [-113, -18], [-113, -99], [-113, -194], [-113, -198], [-112, -12], [-112, -154], [-112, -194], [-111, -6], [-111, -101], [-111, -157], [-111, -201], [-110, -1], [-110, -2], [-110, -102], [-110, -135], [-110, -149], [-110, -154], [-109, 4], [-109, -201], [-108, 10], [-107, 15], [-107, 13], [-106, 20], [-106, 19], [-105, -109], [-105, -136], [-105, -147], [-105, -208], [-101, -115], [-100, 19], [-100, -117], [-99, -119], [-98, 17], [-98, -120], [-98, -142], [-98, -211], [-97, -120], [-97, -142], [-96, 1], [-96, -9], [-96, -211], [-95, 7], [-95, 6], [-95, -9], [-95, -126], [-95, -211], [-94, 14], [-94, 13], [-94, 12], [-94, -6], [-94, -7], [-94, -139], [-93, 7], [-93, 1], [-93, 0], [-93, -1], [-93, -2], [-93, -129], [-92, -130], [-91, -131], [-90, 9], [-90, -132], [-90, -209], [-89, 17], [-88, 21], [-88, 11], [-88, -134], [-87, 10], [-86, 8], [-85, 28], [-85, -208], [-84, 3], [-84, -140], [-83, 11], [-83, 10], [-83, 3], [-83, 2], [-83, -141], [-81, 0], [-81, -207], [-80, -207], [-79, 4], [-79, -16], [-78, 6], [-78, -4], [-78, -5], [-78, -8], [-78, -19], [-77, 25], [-77, 24], [-77, 16], [-77, 14], [-77, 7], [-77, -10], [-77, -23], [-76, 10], [-75, 7], [-75, -205], [-74, 34], [-74, 31], [-74, 28], [-74, 27], [-74, -146], [-73, 22], [-73, 21], [-73, -21], [-73, -206], [-72, -18], [-72, -203], [-71, 43], [-71, -28], [-71, -32], [-71, -203], [-70, 46], [-69, -14], [-68, 54], [-68, 53], [-68, -200], [-66, -198], [-64, -196], [-63, -161], [-63, -194], [-62, -163], [-62, -193], [-61, -165], [-60, -190], [-59, -169], [-59, -188], [-58, -184]]

leaf = [[-198, 210], [-198, 209], [-197, 209], [-197, 208], [-196, 211], [-196, 207], [-196, 206], [-195, 212], [-195, 205], [-194, 212], [-194, 204], [-193, 213], [-193, 204], [-193, 203], [-192, 214], [-192, 213], [-192, 203], [-192, 202], [-191, 215], [-191, 202], [-191, 201], [-190, 216], [-190, 215], [-190, 201], [-190, 200], [-189, 200], [-189, 199], [-188, 218], [-188, 217], [-187, 217], [-187, 198], [-186, 219], [-186, 197], [-186, 195], [-185, 220], [-185, 219], [-185, 196], [-185, 195], [-184, 221], [-184, 220], [-184, 195], [-184, 193], [-184, 192], [-183, 221], [-183, 194], [-183, 190], [-182, 222], [-182, 193], [-182, 192], [-182, 189], [-182, 188], [-181, 223], [-181, 222], [-181, 192], [-181, 191], [-181, 188], [-181, 187], [-180, 223], [-180, 191], [-180, 185], [-179, 224], [-179, 190], [-179, 189], [-179, 183], [-178, 224], [-178, 188], [-178, 187], [-177, 225], [-177, 187], [-177, 186], [-177, 181], [-176, 225], [-176, 185], [-176, 184], [-176, 179], [-176, 178], [-175, 226], [-175, 184], [-175, 183], [-175, 178], [-175, 177], [-174, 227], [-174, 226], [-174, 183], [-174, 182], [-174, 177], [-174, 175], [-174, 140], [-174, 139], [-174, 138], [-174, 137], [-174, 135], [-174, 134], [-174, 133], [-174, 132], [-174, 131], [-174, 130], [-174, 129], [-174, 128], [-173, 227], [-173, 181], [-173, 174], [-173, 148], [-173, 147], [-173, 146], [-173, 145], [-173, 144], [-173, 143], [-173, 142], [-173, 127], [-173, 125], [-173, 124], [-173, 123], [-172, 180], [-172, 171], [-172, 170], [-172, 169], [-172, 168], [-172, 166], [-172, 165], [-172, 163], [-172, 162], [-172, 161], [-172, 160], [-172, 158], [-172, 156], [-172, 155], [-172, 154], [-172, 153], [-172, 152], [-172, 151], [-172, 150], [-172, 121], [-172, 120], [-172, 119], [-172, 118], [-171, 227], [-171, 180], [-171, 179], [-171, 173], [-171, 117], [-171, 116], [-170, 228], [-170, 227], [-170, 179], [-170, 178], [-170, 170], [-170, 169], [-170, 168], [-170, 167], [-170, 166], [-170, 115], [-169, 227], [-169, 178], [-169, 170], [-169, 165], [-169, 164], [-169, 163], [-169, 162], [-169, 160], [-169, 159], [-169, 114], [-169, 113], [-168, 228], [-168, 227], [-168, 177], [-168, 169], [-168, 168], [-168, 158], [-168, 157], [-168, 156], [-168, 155], [-168, 154], [-168, 113], [-168, 112], [-167, 228], [-167, 227], [-167, 177], [-167, 176], [-167, 168], [-167, 167], [-167, 150], [-167, 149], [-167, 148], [-167, 147], [-167, 146], [-167, 145], [-167, 112], [-167, 111], [-166, 228], [-166, 227], [-166, 176], [-166, 167], [-166, 166], [-166, 143], [-166, 140], [-166, 139], [-166, 138], [-166, 137], [-166, 136], [-166, 110], [-165, 228], [-165, 227], [-165, 175], [-165, 174], [-165, 166], [-165, 165], [-165, 131], [-165, 130], [-165, 129], [-165, 128], [-165, 127], [-165, 126], [-165, 125], [-165, 124], [-165, 123], [-165, 122], [-165, 109], [-164, 228], [-164, 200], [-164, 199], [-164, 198], [-164, 173], [-164, 164], [-164, 119], [-164, 118], [-164, 117], [-164, 116], [-164, 115], [-164, 114], [-164, 108], [-163, 228], [-163, 227], [-163, 200], [-163, 198], [-163, 197], [-163, 196], [-163, 173], [-163, 163], [-163, 113], [-163, 112], [-163, 111], [-163, 109], [-163, 108], [-162, 228], [-162, 227], [-162, 200], [-162, 196], [-162, 195], [-162, 194], [-162, 173], [-162, 172], [-162, 162], [-162, 109], [-162, 108], [-162, 106], [-161, 227], [-161, 200], [-161, 194], [-161, 193], [-161, 192], [-161, 172], [-161, 171], [-161, 161], [-161, 104], [-161, 103], [-160, 228], [-160, 200], [-160, 191], [-160, 190], [-160, 171], [-160, 160], [-160, 103], [-160, 102], [-160, 101], [-159, 228], [-159, 226], [-159, 200], [-159, 189], [-159, 188], [-159, 170], [-159, 159], [-159, 99], [-158, 228], [-158, 226], [-158, 200], [-158, 187], [-158, 186], [-158, 170], [-158, 169], [-158, 158], [-158, 98], [-158, 97], [-158, 96], [-157, 226], [-157, 200], [-157, 185], [-157, 184], [-157, 169], [-157, 168], [-157, 157], [-157, 95], [-157, 88], [-156, 228], [-156, 225], [-156, 200], [-156, 183], [-156, 182], [-156, 168], [-156, 157], [-156, 156], [-156, 93], [-156, 87], [-155, 227], [-155, 225], [-155, 200], [-155, 182], [-155, 167], [-155, 166], [-155, 156], [-155, 155], [-155, 91], [-155, 86], [-155, 84], [-154, 227], [-154, 225], [-154, 200], [-154, 181], [-154, 180], [-154, 179], [-154, 167], [-154, 155], [-154, 154], [-154, 85], [-154, 83], [-153, 227], [-153, 225], [-153, 200], [-153, 178], [-153, 177], [-153, 165], [-153, 154], [-153, 89], [-153, 88], [-153, 84], [-152, 227], [-152, 225], [-152, 200], [-152, 175], [-152, 165], [-152, 164], [-152, 87], [-152, 86], [-151, 227], [-151, 225], [-151, 200], [-151, 174], [-151, 173], [-151, 164], [-151, 163], [-150, 228], [-150, 227], [-150, 225], [-150, 200], [-150, 170], [-150, 169], [-150, 168], [-150, 167], [-150, 166], [-150, 165], [-150, 164], [-150, 163], [-150, 162], [-150, 85], [-150, 84], [-150, 82], [-150, 78], [-149, 228], [-149, 225], [-149, 200], [-149, 163], [-149, 162], [-149, 150], [-149, 83], [-148, 228], [-148, 227], [-148, 225], [-148, 200], [-148, 149], [-148, 81], [-147, 229], [-147, 227], [-147, 225], [-147, 200], [-147, 160], [-147, 149], [-147, 148], [-147, 81], [-147, 65], [-146, 230], [-146, 229], [-146, 227], [-146, 225], [-146, 159], [-146, 148], [-146, 147], [-145, 231], [-145, 230], [-145, 227], [-145, 225], [-145, 200], [-145, 159], [-145, 158], [-145, 147], [-145, 146], [-145, 69], [-144, 232], [-144, 225], [-144, 199], [-144, 157], [-144, 146], [-144, 67], [-143, 233], [-143, 228], [-143, 225], [-143, 199], [-143, 156], [-143, 66], [-142, 233], [-142, 225], [-142, 199], [-142, 77], [-142, 55], [-141, 235], [-141, 234], [-141, 228], [-141, 199], [-141, 143], [-141, 76], [-141, 56], [-140, 236], [-140, 226], [-140, 199], [-140, 153], [-140, 143], [-140, 142], [-140, 65], [-140, 57], [-139, 237], [-139, 228], [-139, 199], [-139, 152], [-139, 142], [-139, 58], [-138, 226], [-138, 199], [-138, 151], [-138, 59], [-137, 241], [-137, 240], [-137, 226], [-137, 151], [-137, 150], [-137, 140], [-136, 243], [-136, 228], [-136, 226], [-136, 202], [-136, 198], [-136, 150], [-136, 149], [-136, 140], [-135, 244], [-135, 225], [-135, 204], [-135, 203], [-135, 148], [-135, 139], [-134, 244], [-134, 227], [-134, 225], [-134, 205], [-134, 204], [-134, 198], [-134, 148], [-134, 147], [-134, 139], [-134, 138], [-134, 71], [-133, 245], [-133, 227], [-133, 225], [-133, 207], [-133, 206], [-133, 200], [-133, 147], [-133, 146], [-133, 138], [-132, 246], [-132, 227], [-132, 225], [-132, 208], [-132, 207], [-132, 202], [-132, 201], [-132, 200], [-132, 197], [-132, 138], [-132, 137], [-131, 246], [-131, 227], [-131, 224], [-131, 209], [-131, 204], [-131, 203], [-131, 197], [-131, 144], [-131, 137], [-130, 247], [-130, 246], [-130, 227], [-130, 224], [-130, 211], [-130, 210], [-130, 206], [-130, 144], [-130, 143], [-130, 136], [-129, 223], [-129, 212], [-129, 211], [-129, 208], [-129, 143], [-129, 136], [-129, 135], [-129, 97], [-129, 96], [-129, 95], [-129, 94], [-129, 92], [-129, 91], [-129, 90], [-129, 89], [-129, 88], [-129, 86], [-129, 85], [-129, 68], [-128, 246], [-128, 245], [-128, 226], [-128, 213], [-128, 212], [-128, 196], [-128, 195], [-128, 141], [-128, 135], [-128, 100], [-128, 98], [-128, 83], [-128, 82], [-127, 246], [-127, 244], [-127, 226], [-127, 225], [-127, 222], [-127, 221], [-127, 214], [-127, 213], [-127, 210], [-127, 141], [-127, 140], [-127, 135], [-127, 102], [-127, 101], [-127, 82], [-127, 81], [-127, 80], [-126, 246], [-126, 244], [-126, 225], [-126, 221], [-126, 215], [-126, 214], [-126, 212], [-126, 195], [-126, 194], [-126, 139], [-126, 133], [-126, 103], [-126, 84], [-126, 79], [-126, 78], [-125, 245], [-125, 243], [-125, 242], [-125, 225], [-125, 224], [-125, 220], [-125, 216], [-125, 213], [-125, 212], [-125, 139], [-125, 138], [-125, 133], [-125, 106], [-125, 105], [-125, 104], [-125, 76], [-124, 244], [-124, 240], [-124, 224], [-124, 219], [-124, 217], [-124, 216], [-124, 214], [-124, 194], [-124, 138], [-124, 137], [-124, 133], [-124, 132], [-124, 107], [-124, 106], [-124, 75], [-123, 244], [-123, 243], [-123, 240], [-123, 217], [-123, 215], [-123, 193], [-123, 192], [-123, 137], [-123, 136], [-123, 132], [-123, 131], [-123, 109], [-123, 108], [-123, 74], [-123, 73], [-123, 62], [-122, 243], [-122, 239], [-122, 222], [-122, 218], [-122, 217], [-122, 215], [-122, 214], [-122, 212], [-122, 193], [-122, 136], [-122, 135], [-122, 131], [-122, 109], [-122, 72], [-121, 242], [-121, 239], [-121, 238], [-121, 217], [-121, 214], [-121, 213], [-121, 208], [-121, 193], [-121, 192], [-121, 191], [-121, 135], [-121, 134], [-121, 130], [-121, 111], [-121, 110], [-121, 71], [-121, 70], [-120, 241], [-120, 239], [-120, 220], [-120, 218], [-120, 213], [-120, 212], [-120, 211], [-120, 207], [-120, 206], [-120, 205], [-120, 204], [-120, 191], [-120, 190], [-120, 130], [-120, 129], [-120, 70], [-120, 69], [-120, 63], [-119, 241], [-119, 221], [-119, 219], [-119, 202], [-119, 191], [-119, 190], [-119, 132], [-119, 129], [-119, 69], [-119, 68], [-119, 63], [-118, 241], [-118, 221], [-118, 220], [-118, 209], [-118, 207], [-118, 201], [-118, 200], [-118, 199], [-118, 190], [-118, 189], [-118, 188], [-118, 132], [-118, 129], [-118, 115], [-118, 114], [-118, 68], [-118, 67], [-117, 241], [-117, 223], [-117, 221], [-117, 213], [-117, 207], [-117, 206], [-117, 198], [-117, 197], [-117, 196], [-117, 189], [-117, 188], [-117, 131], [-117, 128], [-117, 115], [-117, 67], [-117, 66], [-116, 241], [-116, 238], [-116, 224], [-116, 223], [-116, 222], [-116, 205], [-116, 204], [-116, 195], [-116, 194], [-116, 189], [-116, 187], [-116, 186], [-116, 130], [-116, 129], [-116, 127], [-116, 116], [-116, 66], [-116, 65], [-115, 241], [-115, 238], [-115, 225], [-115, 224], [-115, 223], [-115, 204], [-115, 203], [-115, 193], [-115, 191], [-115, 188], [-115, 186], [-115, 129], [-115, 128], [-115, 126], [-115, 117], [-115, 65], [-114, 239], [-114, 226], [-114, 224], [-114, 202], [-114, 190], [-114, 189], [-114, 187], [-114, 185], [-114, 128], [-114, 127], [-114, 126], [-114, 122], [-114, 118], [-114, 64], [-113, 242], [-113, 239], [-113, 227], [-113, 225], [-113, 224], [-113, 202], [-113, 201], [-113, 189], [-113, 188], [-113, 187], [-113, 186], [-113, 184], [-113, 126], [-113, 119], [-113, 64], [-112, 242], [-112, 239], [-112, 228], [-112, 226], [-112, 225], [-112, 212], [-112, 211], [-112, 209], [-112, 208], [-112, 201], [-112, 200], [-112, 187], [-112, 185], [-112, 184], [-112, 183], [-112, 125], [-112, 124], [-112, 121], [-112, 120], [-111, 243], [-111, 229], [-111, 208], [-111, 207], [-111, 206], [-111, 200], [-111, 199], [-111, 185], [-111, 183], [-111, 182], [-111, 125], [-111, 121], [-111, 62], [-111, 61], [-110, 244], [-110, 242], [-110, 229], [-110, 227], [-110, 214], [-110, 205], [-110, 204], [-110, 202], [-110, 199], [-110, 184], [-110, 124], [-110, 62], [-110, 61], [-109, 246], [-109, 242], [-109, 230], [-109, 215], [-109, 203], [-109, 202], [-109, 198], [-109, 183], [-109, 181], [-109, 61], [-108, 247], [-108, 229], [-108, 216], [-108, 201], [-108, 200], [-108, 197], [-108, 183], [-108, 181], [-108, 180], [-108, 124], [-107, 248], [-107, 247], [-107, 232], [-107, 230], [-107, 218], [-107, 217], [-107, 199], [-107, 197], [-107, 196], [-107, 183], [-107, 180], [-107, 125], [-107, 124], [-106, 249], [-106, 233], [-106, 230], [-106, 218], [-106, 208], [-106, 196], [-106, 182], [-106, 126], [-106, 125], [-106, 60], [-105, 250], [-105, 249], [-105, 233], [-105, 232], [-105, 219], [-105, 209], [-105, 208], [-105, 207], [-105, 196], [-105, 179], [-105, 127], [-105, 126], [-104, 251], [-104, 234], [-104, 220], [-104, 207], [-104, 195], [-104, 181], [-104, 179], [-104, 178], [-104, 128], [-104, 127], [-103, 249], [-103, 234], [-103, 233], [-103, 222], [-103, 206], [-103, 205], [-103, 193], [-103, 181], [-103, 178], [-103, 128], [-102, 249], [-102, 248], [-102, 242], [-102, 241], [-102, 240], [-102, 239], [-102, 235], [-102, 234], [-102, 233], [-102, 224], [-102, 223], [-102, 209], [-102, 205], [-102, 181], [-102, 180], [-102, 178], [-102, 177], [-101, 247], [-101, 246], [-101, 245], [-101, 244], [-101, 243], [-101, 236], [-101, 235], [-101, 234], [-101, 225], [-101, 224], [-101, 210], [-101, 204], [-101, 182], [-101, 180], [-101, 177], [-101, 130], [-101, 58], [-100, 238], [-100, 235], [-100, 226], [-100, 225], [-100, 210], [-100, 192], [-100, 191], [-100, 180], [-100, 176], [-100, 131], [-100, 130], [-99, 238], [-99, 237], [-99, 236], [-99, 211], [-99, 202], [-99, 186], [-99, 184], [-99, 179], [-99, 176], [-99, 133], [-99, 132], [-98, 236], [-98, 226], [-98, 213], [-98, 211], [-98, 201], [-98, 190], [-98, 185], [-98, 184], [-98, 179], [-98, 175], [-98, 133], [-98, 132], [-97, 237], [-97, 227], [-97, 213], [-97, 206], [-97, 201], [-97, 200], [-97, 190], [-97, 189], [-97, 185], [-97, 175], [-97, 134], [-97, 57], [-96, 237], [-96, 227], [-96, 214], [-96, 207], [-96, 206], [-96, 200], [-96, 199], [-96, 189], [-96, 188], [-96, 186], [-96, 178], [-96, 175], [-96, 135], [-96, 134], [-96, 57], [-95, 237], [-95, 214], [-95, 207], [-95, 206], [-95, 199], [-95, 188], [-95, 187], [-95, 186], [-95, 178], [-95, 174], [-95, 136], [-94, 237], [-94, 227], [-94, 215], [-94, 188], [-94, 187], [-94, 177], [-94, 174], [-94, 173], [-93, 205], [-93, 197], [-93, 187], [-93, 177], [-93, 173], [-93, 137], [-92, 237], [-92, 215], [-92, 205], [-92, 196], [-92, 188], [-92, 177], [-92, 173], [-92, 139], [-92, 138], [-91, 226], [-91, 215], [-91, 207], [-91, 205], [-91, 188], [-91, 172], [-91, 140], [-90, 226], [-90, 215], [-90, 205], [-90, 195], [-90, 176], [-90, 172], [-90, 140], [-89, 237], [-89, 226], [-89, 215], [-89, 207], [-89, 205], [-89, 195], [-89, 189], [-89, 176], [-89, 172], [-89, 141], [-88, 237], [-88, 226], [-88, 204], [-88, 175], [-88, 171], [-88, 141], [-87, 237], [-87, 225], [-87, 214], [-87, 204], [-87, 195], [-87, 175], [-87, 171], [-87, 142], [-86, 237], [-86, 225], [-86, 214], [-86, 204], [-86, 195], [-86, 175], [-86, 171], [-85, 237], [-85, 214], [-85, 207], [-85, 204], [-85, 190], [-85, 174], [-85, 144], [-84, 238], [-84, 213], [-84, 203], [-84, 195], [-84, 190], [-84, 174], [-84, 170], [-83, 238], [-83, 224], [-83, 213], [-83, 195], [-83, 190], [-83, 170], [-83, 146], [-83, 145], [-82, 224], [-82, 212], [-82, 208], [-82, 203], [-82, 195], [-82, 173], [-82, 170], [-82, 169], [-82, 57], [-81, 239], [-81, 224], [-81, 212], [-81, 211], [-81, 208], [-81, 203], [-81, 195], [-81, 191], [-81, 173], [-81, 169], [-81, 147], [-80, 239], [-80, 223], [-80, 211], [-80, 208], [-80, 203], [-80, 195], [-80, 172], [-80, 169], [-80, 147], [-79, 240], [-79, 223], [-79, 211], [-79, 208], [-79, 203], [-79, 191], [-79, 172], [-79, 169], [-79, 148], [-78, 240], [-78, 223], [-78, 222], [-78, 210], [-78, 208], [-78, 203], [-78, 194], [-78, 191], [-78, 171], [-78, 168], [-78, 58], [-77, 241], [-77, 222], [-77, 210], [-77, 208], [-77, 203], [-77, 193], [-77, 171], [-77, 168], [-77, 149], [-76, 242], [-76, 221], [-76, 209], [-76, 202], [-76, 193], [-76, 192], [-76, 170], [-76, 168], [-75, 242], [-75, 241], [-75, 220], [-75, 219], [-75, 218], [-75, 203], [-75, 193], [-75, 192], [-75, 169], [-75, 167], [-75, 151], [-74, 218], [-74, 217], [-74, 216], [-74, 209], [-74, 203], [-74, 192], [-74, 169], [-74, 151], [-73, 216], [-73, 215], [-73, 214], [-73, 209], [-73, 194], [-73, 193], [-73, 168], [-73, 167], [-73, 152], [-72, 242], [-72, 237], [-72, 209], [-72, 202], [-72, 196], [-72, 195], [-72, 193], [-72, 168], [-72, 167], [-72, 166], [-72, 152], [-72, 60], [-71, 240], [-71, 212], [-71, 210], [-71, 202], [-71, 197], [-71, 195], [-71, 166], [-71, 153], [-70, 212], [-70, 211], [-70, 210], [-70, 202], [-70, 199], [-70, 198], [-70, 197], [-70, 194], [-70, 166], [-70, 165], [-70, 153], [-70, 61], [-69, 238], [-69, 237], [-69, 211], [-69, 201], [-69, 200], [-69, 195], [-69, 194], [-69, 166], [-69, 165], [-69, 154], [-69, 61], [-69, 60], [-68, 236], [-68, 209], [-68, 200], [-68, 195], [-68, 166], [-68, 164], [-68, 62], [-68, 58], [-68, 55], [-67, 236], [-67, 235], [-67, 211], [-67, 208], [-67, 199], [-67, 195], [-67, 166], [-67, 165], [-67, 155], [-67, 62], [-66, 235], [-66, 210], [-66, 207], [-66, 168], [-66, 167], [-66, 155], [-66, 63], [-65, 234], [-65, 211], [-65, 207], [-65, 206], [-65, 196], [-65, 170], [-65, 63], [-64, 234], [-64, 211], [-64, 171], [-64, 170], [-64, 156], [-64, 64], [-63, 211], [-63, 197], [-63, 156], [-63, 65], [-62, 211], [-62, 205], [-62, 197], [-62, 157], [-62, 65], [-61, 211], [-61, 204], [-61, 197], [-61, 175], [-61, 174], [-61, 173], [-61, 157], [-60, 233], [-60, 210], [-60, 204], [-60, 203], [-60, 197], [-60, 176], [-60, 175], [-60, 160], [-60, 157], [-60, 67], [-59, 233], [-59, 210], [-59, 202], [-59, 201], [-59, 197], [-59, 177], [-59, 176], [-59, 159], [-59, 158], [-59, 157], [-59, 72], [-59, 68], [-58, 232], [-58, 200], [-58, 199], [-58, 198], [-58, 177], [-58, 158], [-58, 69], [-57, 210], [-57, 197], [-57, 179], [-57, 178], [-56, 232], [-56, 231], [-56, 209], [-56, 198], [-56, 197], [-56, 180], [-56, 159], [-56, 158], [-55, 230], [-55, 209], [-55, 199], [-55, 181], [-55, 180], [-55, 159], [-55, 158], [-55, 73], [-55, 72], [-54, 231], [-54, 230], [-54, 200], [-54, 197], [-54, 181], [-54, 159], [-54, 158], [-54, 74], [-54, 73], [-53, 231], [-53, 229], [-53, 228], [-53, 207], [-53, 200], [-53, 197], [-53, 183], [-53, 182], [-53, 160], [-53, 158], [-53, 75], [-53, 74], [-52, 230], [-52, 207], [-52, 206], [-52, 201], [-52, 200], [-52, 183], [-52, 160], [-52, 158], [-52, 76], [-52, 75], [-51, 229], [-51, 226], [-51, 206], [-51, 205], [-51, 201], [-51, 197], [-51, 184], [-50, 229], [-50, 227], [-50, 205], [-50, 204], [-50, 202], [-50, 197], [-50, 185], [-50, 161], [-50, 159], [-50, 158], [-50, 79], [-50, 78], [-49, 228], [-49, 226], [-49, 225], [-49, 224], [-49, 223], [-49, 203], [-49, 202], [-49, 197], [-49, 161], [-49, 81], [-49, 80], [-48, 228], [-48, 225], [-48, 224], [-48, 221], [-48, 203], [-48, 197], [-48, 159], [-47, 227], [-47, 224], [-47, 223], [-47, 204], [-47, 197], [-47, 187], [-47, 161], [-47, 159], [-47, 84], [-47, 83], [-46, 226], [-46, 223], [-46, 217], [-46, 216], [-46, 204], [-46, 197], [-46, 187], [-46, 159], [-46, 86], [-46, 85], [-45, 226], [-45, 225], [-45, 222], [-45, 215], [-45, 205], [-45, 188], [-45, 159], [-45, 87], [-44, 221], [-44, 215], [-44, 206], [-44, 197], [-44, 196], [-44, 162], [-44, 159], [-44, 90], [-44, 89], [-43, 221], [-43, 207], [-43, 198], [-43, 197], [-43, 196], [-43, 190], [-43, 162], [-43, 91], [-42, 224], [-42, 221], [-42, 214], [-42, 208], [-42, 200], [-42, 199], [-42, 198], [-42, 196], [-42, 195], [-42, 190], [-42, 163], [-42, 159], [-42, 94], [-42, 93], [-41, 224], [-41, 221], [-41, 214], [-41, 209], [-41, 208], [-41, 203], [-41, 202], [-41, 201], [-41, 195], [-41, 191], [-41, 163], [-41, 97], [-41, 96], [-40, 224], [-40, 221], [-40, 214], [-40, 210], [-40, 207], [-40, 206], [-40, 205], [-40, 204], [-40, 203], [-40, 192], [-40, 163], [-40, 159], [-40, 100], [-40, 98], [-39, 223], [-39, 221], [-39, 214], [-39, 210], [-39, 209], [-39, 195], [-39, 192], [-39, 164], [-39, 159], [-39, 102], [-39, 101], [-38, 223], [-38, 221], [-38, 214], [-38, 212], [-38, 195], [-38, 193], [-38, 164], [-38, 163], [-38, 159], [-38, 106], [-38, 105], [-38, 104], [-38, 103], [-37, 223], [-37, 221], [-37, 214], [-37, 213], [-37, 195], [-37, 194], [-37, 166], [-37, 165], [-37, 159], [-37, 108], [-37, 107], [-37, 106], [-36, 223], [-36, 222], [-36, 167], [-36, 166], [-36, 164], [-36, 112], [-36, 111], [-36, 110], [-36, 109], [-35, 223], [-35, 222], [-35, 196], [-35, 169], [-35, 168], [-35, 116], [-35, 115], [-35, 114], [-34, 223], [-34, 222], [-34, 197], [-34, 196], [-34, 170], [-34, 164], [-34, 160], [-34, 120], [-34, 119], [-34, 118], [-34, 117], [-33, 223], [-33, 198], [-33, 175], [-33, 174], [-33, 125], [-33, 124], [-33, 123], [-33, 122], [-33, 121], [-32, 199], [-32, 198], [-32, 179], [-32, 178], [-32, 177], [-32, 176], [-32, 164], [-32, 160], [-32, 127], [-32, 126], [-31, 223], [-31, 200], [-31, 182], [-31, 181], [-31, 164], [-31, 160], [-31, 129], [-30, 223], [-30, 201], [-30, 200], [-30, 187], [-30, 186], [-30, 185], [-30, 184], [-30, 164], [-30, 160], [-30, 131], [-30, 130], [-29, 223], [-29, 202], [-29, 201], [-29, 192], [-29, 191], [-29, 190], [-29, 189], [-29, 164], [-29, 160], [-29, 133], [-29, 132], [-28, 223], [-28, 204], [-28, 203], [-28, 194], [-28, 164], [-28, 160], [-28, 133], [-27, 223], [-27, 196], [-27, 195], [-27, 194], [-27, 164], [-27, 160], [-27, 135], [-27, 134], [-26, 223], [-26, 206], [-26, 205], [-26, 199], [-26, 198], [-26, 194], [-26, 193], [-26, 164], [-26, 161], [-26, 137], [-26, 136], [-25, 223], [-25, 213], [-25, 208], [-25, 207], [-25, 200], [-25, 199], [-25, 194], [-25, 164], [-25, 161], [-25, 138], [-25, 137], [-24, 223], [-24, 209], [-24, 202], [-24, 201], [-24, 164], [-24, 139], [-23, 223], [-23, 210], [-23, 207], [-23, 204], [-23, 203], [-23, 193], [-23, 164], [-23, 161], [-23, 140], [-23, 139], [-22, 223], [-22, 213], [-22, 212], [-22, 209], [-22, 208], [-22, 207], [-22, 206], [-22, 205], [-22, 161], [-22, 141], [-21, 216], [-21, 214], [-21, 213], [-21, 211], [-21, 210], [-21, 192], [-21, 165], [-21, 161], [-21, 142], [-21, 141], [-20, 223], [-20, 222], [-20, 221], [-20, 219], [-20, 216], [-20, 215], [-20, 191], [-20, 190], [-20, 165], [-20, 162], [-20, 143], [-20, 142], [-19, 191], [-19, 190], [-19, 189], [-19, 165], [-19, 162], [-19, 143], [-18, 190], [-18, 189], [-18, 165], [-18, 162], [-18, 144], [-17, 190], [-17, 189], [-17, 188], [-17, 165], [-17, 162], [-17, 145], [-16, 189], [-16, 188], [-16, 187], [-16, 165], [-16, 146], [-15, 188], [-15, 187], [-15, 186], [-15, 165], [-15, 163], [-15, 146], [-14, 188], [-14, 185], [-14, 184], [-14, 163], [-14, 147], [-13, 184], [-13, 183], [-13, 163], [-12, 186], [-12, 185], [-12, 166], [-12, 164], [-12, 149], [-11, 185], [-11, 181], [-11, 180], [-11, 166], [-11, 164], [-11, 149], [-10, 184], [-10, 183], [-10, 166], [-10, 164], [-10, 150], [-9, 183], [-9, 181], [-9, 166], [-9, 164], [-9, 150], [-8, 181], [-8, 180], [-8, 177], [-8, 165], [-8, 151], [-7, 177], [-7, 176], [-7, 167], [-7, 165], [-7, 152], [-6, 178], [-6, 176], [-6, 167], [-6, 165], [-6, 153], [-5, 177], [-5, 175], [-5, 167], [-5, 154], [-5, 153], [-4, 177], [-4, 175], [-4, 167], [-4, 166], [-4, 155], [-4, 154], [-3, 176], [-3, 174], [-3, 167], [-3, 166], [-3, 156], [-2, 168], [-2, 167], [-2, 157], [-2, 156], [-1, 176], [-1, 174], [-1, 168], [-1, 167], [-1, 157], [0, 174], [0, 168], [0, 167], [1, 176], [1, 174], [1, 168], [1, 159], [2, 176], [2, 174], [2, 160], [2, 159], [3, 161], [4, 175], [4, 174], [4, 162], [5, 174], [5, 168], [5, 163], [6, 164], [7, 169], [7, 164], [9, 173], [9, 169], [9, 166], [10, 171], [10, 169], [10, 167], [11, 169], [11, 168]]

str0 = "你曾问我程序画好之后是什么"
str1 = "我回答说画好之后是一朵花"
str2 = "准确地说, 它是一朵"
str3 = " 玫瑰 "
str4 = "我不会突然想到去尝试图像处理"
str5 = "尝试的原因就是我想绘这朵玫瑰"
str6 = "玫瑰予人， 这段代码为你而写"

str7 = "喜欢处处努力上进、即使生活匆忙也依旧精致的你"
str8 = "美丽的玫瑰送给美丽的你"

#单字绘制函数
def write(str):
    for i in str:
        turtle.write(i, move = True, font = 8)
        time.sleep(0.3)

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def do(x, y, str):
    time.sleep(0.2)
    move(x, y)
    write(str)

#窗口配置
turtle.setup(1050, 750, 0, 0)

#绘制前的话
turtle.color("SeaGreen4")
do(130, 300, str0)
do(110, 250, str1)
do(110, 200, str2)
time.sleep(0.2)
turtle.color("red")
write(str3)
turtle.color("SeaGreen4")
do(110, 120, str4)
do(110, 70, str5)
do(110, 20, str6)

#依据坐标绘制玫瑰轮廓
turtle.color("green")
for coordinate in rose:
    turtle.penup()
    turtle.goto(coordinate[0], coordinate[1])
    turtle.pendown()
    turtle.forward(1)

turtle.color("red")
for coordinate in leaf:
    turtle.penup()
    turtle.goto(coordinate[0], coordinate[1])
    turtle.pendown()
    turtle.forward(1)

#绘制后的话
turtle.color("SeaGreen4")
do(110, -60, str7)
turtle.color("red")
do(110, -110, str8)

turtle.showturtle()
input("Any key to quit...")
