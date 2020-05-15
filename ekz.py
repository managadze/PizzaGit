def FillPic(image, sr, sc, newColor):
    prevColor = image[sr][sc]
    if prevColor == newColor:
        return image
    else:
        image = req(sr,sc, prevColor, image, newColor)
        return image

def req(row, col, prevC, image, newC):
    if image[row][col] == prevC:
        image[row][col] = newC
        if row >= 1:
            req(row-1, col, prevC, image, newC)
        if col >= 1:
            req(row, col-1, prevC, image, newC)
        if row+1 < len(image):
            req(row+1, col, prevC, image, newC)
        if col+1 < len(image[0]):
            req(row, col+1, prevC, image, newC)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
newImage = FillPic(image, 1,1,2)
print(newImage)
