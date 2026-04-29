import event from "events";
console.log("At the start....");
let eventEmitter = new event.EventEmitter();

eventEmitter.on("hi",function(){
    console.log("Hii.....");
});

eventEmitter.on("hello",function(){
    console.log("Hello....");
});
eventEmitter.emit("hi");
eventEmitter.emit("hi");
eventEmitter.emit("hi");
eventEmitter.emit("hello");
console.log("At the end....");
