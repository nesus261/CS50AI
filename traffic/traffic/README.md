First, I checked the lecture model with changed input_shape to (IMG_WIDTH, IMG_HEIGHT, 3) and Dense output layer units to NUM_CATEGORIES. The results were as follows:  
accuracy: 0.7823  
evaluate accuracy: 0.9486

I removed pool_size=(2, 2) from MaxPooling as it is the default value. I added the Conv2D layer with MaxPooling twice. I set the number of filters in the Conv2D layers ascending - 16, 32, 64. The efficiency increased to the following results:  
accuracy: 0.9318  
evaluate accuracy: 0.9708

The model.summary() method shows a decrease in the number of trained parameters from 809,387 to 102,987 with greater efficiency -> more conv2d = more recognized features
Despite the lower complexity (mainly due to the greater number of MaxPooling layers), better results are obtained.

For the test, I changed MaxPooling to AveragePooling. Efficiency dropped to the following results:  
accuracy: 0.8605  
evaluate accuracy: 0.9269  
MaxPooling makes the picture clearer and performs better than AveragePooling on this data set.

I went back to MaxPooling. I added another Conv2D layer with filter 128 and MaxPooling. This improved the results to the following:  
accuracy: 0.9727  
evaluate accuracy: 0.9780

Due to the reduction of the output shape after applying the combination of Conv2D and MaxPooling layers, it is not possible to add more of these layers, except by changing the filters/kernels. Then I experimented with the size of kernels in Conv2D. I checked 3-5, but it didn't have much effect on performance on this dataset, so I went back to the default 3. Then I replaced the activation functions with sigmoid and tanh in the Dense layer and Conv2D layers. Relu was found to work best on Conv2D layers. Meanwhile, tanh turned out to be the best on the Dense layer.

Then I looked again at model.summary() and shapes on different layers. The fourth Conv2D layer didn't change shape, so I deleted it and changed the filters in the other Conv2D layers to 32, 64, 128. I also tested a different number of units on the Dense layer as well as more than one Dense layer. One layer of Dense with 86 units worked best. The results I got are as follows:  
accuracy: 0.9949  
evaluate accuracy: 0.9934
