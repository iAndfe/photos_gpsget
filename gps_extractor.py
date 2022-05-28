# Function: Convert latitude/longitude to decimals
def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees

# Function: Obtain GPS metadata from photos
def gps_extractor():
    # Using command: pip install package_name
    # Install packages: exif, pandas
    # Make sure working directory is in path file

    from os import listdir
    from os.path import isfile, join
    from exif import Image
    import pandas

    # Create dataframe with Metadata as columns
    Labels = ["index", "file", "model", "datetime", "_gps_ifd_pointer", "make", "datetime_original", "gps_img_direction_ref",
            "gps_img_direction", "gps_latitude", "gps_longitude", "gps_altitude"]
    df = pandas.DataFrame(columns = Labels)

    # Create list of image names
    imageFilenames = [f for f in listdir("Photos") if isfile(join("Photos", f))]

    ## Obtain Metadata from photos and store in dataframe
    for x in range(0, len(imageFilenames)):

        # Upload photo
        img_path = "Photos/" + imageFilenames[x]
        PhotoData = [0]*(len(Labels))
        
        # Extract Metadata
        with open(img_path, "rb") as src:
                img = Image(src)
                    
                # Obtain Metadata from photo
                PhotoData[0] = x
                PhotoData[1] = imageFilenames[x]
                try:
                    PhotoData[2] = img.model
                except:
                    error = 1
                try:
                    PhotoData[3] = img.datetime
                except:
                    error = 1
                try:
                    PhotoData[4] = img._gps_ifd_pointer
                except:
                    error = 1
                try:
                    PhotoData[5] = img.make
                except:
                    error = 1
                try:
                    PhotoData[6] = img.datetime_original
                except:
                    error = 1
                try:
                    PhotoData[7] = img.gps_img_direction_ref
                except:
                    error = 1
                try:
                    PhotoData[8] = img.gps_img_direction
                except:
                    error = 1
                try:
                    PhotoData[9] = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
                except:
                    error = 1
                try:
                    PhotoData[10] = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
                except:
                    error = 1
                try:
                    PhotoData[11] = img.gps_altitude
                except:
                    error = 1

                # Store Metadata
                for y in range(len(PhotoData)):
                    df.loc[x, Labels[y]] = PhotoData[y]

    return df