n="javascriptloops"

for (let i=0;i<n.length;i++){

    if (n[i].toLowerCase()=='a'|n[i].toLowerCase()=='e'|n[i].toLowerCase()=='o'|n[i].toLowerCase()=='u'|n[i].toLowerCase()=='i'){
        console.log(n[i])
    }

}
for (let i=0;i<n.length;i++){

    if (!(n[i].toLowerCase()=='a'|n[i].toLowerCase()=='e'|n[i].toLowerCase()=='o'|n[i].toLowerCase()=='u'|n[i].toLowerCase()=='i')){
        console.log(n[i])
    }

}