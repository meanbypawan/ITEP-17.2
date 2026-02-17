setTimeout(()=>{ // Macro Task queue 3
    console.log("Time out executed....");
},0);

setImmediate(()=>{ // Macro Task Queue  4
    console.log("Set immediated executed....");
});

process.nextTick(()=>{ // Tick 1
    console.log("Tick executed....");
});

Promise.resolve().then(()=>{ // Micro Task Queue 2
    console.log("Promise executed....");
});