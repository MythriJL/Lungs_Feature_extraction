import DicomRead
import dcm2png

if __name__ == "__main__":
    ds = (DicomRead.read("/Users/mythrijl/Documents/VII/Project/Codes/Feature Extraction/image","0000a175-0e68-4ca4-b1af-167204a7e0bc.dcm"))
    print(dcm2png.convert_to_png(ds))