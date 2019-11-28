def part_2():
    images = []
    histogram_dict = {}
    list_of_best_matches = []
    list_queries = []
    print(type(histogram_dict))
    path_images = os.path.join(os.getcwd(), 'COLOR_IMAGES/')
    for image in os.listdir(path_images):
        images.append(image)
    print(len(images))

    for image in images:
        img = cv2.imread("%s%s"%(path_images, image))
        hist_img = compute_histogram(img)
        #list_histograms.append(hist_img)
        histogram_dict.update({image:hist_img})
    
    #Part 2 Subpart b)
    print("Part2 Subpart B")
    h_image_1_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '202.jpg')))
    h_image_2_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '302.jpg')))
    h_image_3_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '505.jpg')))
    h_image_4_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '602.jpg')))
    h_image_5_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '720.jpg')))
    h_image_6_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '807.jpg')))
    h_image_7_1  =  compute_histogram(cv2.imread("%s%s"%(path_images, '920.jpg')))
    print("Best 4 Matches for Image1:", best_4_matches(h_image_1_1,histogram_dict))
    print("Best 4 Matches for Image2:", best_4_matches(h_image_2_1,histogram_dict))
    print("Best 4 Matches for Image3:", best_4_matches(h_image_3_1,histogram_dict))
    print("Best 4 Matches for Image4:", best_4_matches(h_image_4_1,histogram_dict))
    print("Best 4 Matches for Image5:", best_4_matches(h_image_5_1,histogram_dict))
    print("Best 4 Matches for Image6:", best_4_matches(h_image_6_1,histogram_dict))
    print("Best 4 Matches for Image7:", best_4_matches(h_image_7_1,histogram_dict))
    
    #Part 2 Subpart C)
    print("Part2 Subpart C\n\n")
    h_image_1_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '200.jpg')))
    h_image_2_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '306.jpg')))
    h_image_3_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '578.jpg')))
    h_image_4_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '652.jpg')))
    h_image_5_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '743.jpg')))
    h_image_6_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '856.jpg')))
    h_image_7_2  =  compute_histogram(cv2.imread("%s%s"%(path_images, '990.jpg')))
    print("Best 4 Matches for Image1:", best_4_matches(h_image_1_2,histogram_dict))
    print("Best 4 Matches for Image2:", best_4_matches(h_image_2_2,histogram_dict))
    print("Best 4 Matches for Image3:", best_4_matches(h_image_3_2,histogram_dict))
    print("Best 4 Matches for Image4:", best_4_matches(h_image_4_2,histogram_dict))
    print("Best 4 Matches for Image5:", best_4_matches(h_image_5_2,histogram_dict))
    print("Best 4 Matches for Image6:", best_4_matches(h_image_6_2,histogram_dict))
    print("Best 4 Matches for Image7:", best_4_matches(h_image_7_2,histogram_dict)) 
    
    
def compute_histogram(image):
    histr = []
   
    for channel_idx in range(3):
        hist_image = cv2.calcHist([image],[channel_idx],None,[32],[0,256])
        histr.append(hist_image)
    hist_array = np.asarray(histr).ravel()

    return hist_array

def histogram_int(h1, h2):
    sum = 0
    for i in range(h1.shape[0]):
        sum += min(h1[i], h2[i])
    
    return sum/np.sum(h1)

def best_4_matches(q_image, histogram_dict):
    intersection_dict = {}
    for key in histogram_dict:
        intersection_dict.update({key:histogram_int(q_image,histogram_dict[key])})
    list_of_best_matches = []
    sorted_d = sorted(intersection_dict.items(), key=operator.itemgetter(1))
    list_of_best_matches = sorted_d[:-6:-1]
    return list_of_best_matches[1:5]    
    
