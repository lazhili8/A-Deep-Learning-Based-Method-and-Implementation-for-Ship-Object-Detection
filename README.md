Abstract: In order to improve the recognition accuracy of ship targets in Synthetic Aperture Radar (SAR) images, this study adopts a data-driven deep learning-based ship detection approach, utilizing YOLOv5, YOLOv7, and YOLOv7-X models to recognize ship targets in the HRSID dataset and a custom-enhanced HRSID dataset for small target detection. The results are presented in a visual format. Simultaneously, the recognition capabilities are extended to ship targets in images, video streams, and real-time camera feeds. The research methodology includes four key aspects: dataset selection and enhancement, selection of deep learning algorithms, development of auxiliary Python scripts for model training, and design and implementation of visualization interfaces. To simplify repetitive tasks in the experimental process and enhance detection convenience, relevant Python scripts and a user interface were designed and implemented to support batch and random insertion of small targets into images, as well as stacking the true and predicted bounding boxes for test samples, significantly improving the ship detection workflow. Experimental results show that using YOLOv7-X combined with the enhanced HRSID dataset achieves a recognition accuracy of 92.53%, with good recognition performance for small targets and ships in complex backgrounds (such as ports), demonstrating a significant improvement in accuracy compared to traditional ship detection methods. 

Keywords: Ship Detection; SAR Images; HRSID Dataset; YOLO Models; Visualization
![image](https://github.com/user-attachments/assets/2f4b6e93-d8f2-43c6-a610-c5478c1550c6)
Numerical curves of Map0.5 and loss for each epoch under multiple experimental conditions

![image](https://github.com/user-attachments/assets/7dc3c44b-a55c-4bed-b2da-70f0d8a29b62)
![image](https://github.com/user-attachments/assets/40ed56d6-b04c-4670-9cf2-0ec24d23423e)
Comparison of test results for the same image under multiple experimental conditions

![image](https://github.com/user-attachments/assets/92b6ae52-60ef-4029-95a0-10b744853c1e)
Visualization effect after detection completion

![image](https://github.com/user-attachments/assets/d6372c74-2dfc-424c-91ae-8f2874b1b05d)
shows the detection results and plays them synchronously with the onginal video

![image](https://github.com/user-attachments/assets/91e91dbf-1f99-483c-a323-d678d75e7866)
Visualization effect of camera detection


