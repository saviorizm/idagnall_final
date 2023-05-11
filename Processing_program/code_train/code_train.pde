  int DIM = 32;
  
void setup() {
  size(1000,1000,P3D);
}

void draw() {
  background(0);
  translate(width/2, height/2);
  for (int i = 0; i < DIM; i++) {
    for (int j = 0; j < DIM; i++) {
      for (int k = 0; k < DIM; i++) {
        float x = map(i, 0, DIM, -100, 100);
        float y = map(j, 0, DIM, -100, 100);
        float z = map(k, 0, DIM, -100, 100);
        stroke(255);
        point(x,y,z);
      }
    }
  }
}

    
