class Car{
    #engine; // dependency
    constructor(engine){
      this.#engine = engine;
    }
}
class Engine{
   #fuelType;
   #hp; 
   constructor(fuleType,hp){
     this.#fuelType = fuleType;
     this.#hp = hp;
   }  
}

let engine = new Engine("Petrol","1200cc")
let obj = new Car(engine);
let obj2 = new Car();