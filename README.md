This chessboard occupancy detection program isn't perfect, but it's a great start to determining occupancy in images with defined regions!
While this method can be used to detect occupancy in a static image, it is my intention to later apply this to a live video feed, using ArUco markers to locate the four corners of the board, and then mathematically defining ROIs using those pixel locations. 
Please note that for the specific board I used, the percent of black pixels necessary to classify white squares as "occupied" is >= 45% because the Otsu thresholding method adds black pixels where the wood grain is on the board. The Otsu thresholding method is NOT optimal for a wooden board for this reason, and adaptive thresholding would be a preferable method.
Also, the squares of the board I used are brown and tan, and the chess pieces are dark brown and light tan.
Percentages to classify as "occupied" will have to be adjusted for different boards/pieces, since some are more reflective or use other colors.

Good luck with the project you're working on!
