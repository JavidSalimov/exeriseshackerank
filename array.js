// a= Math.max(...[3,4,2,3,4,5,6]);


// console.log(a)
// const result = words.filter(word => word.length > 6);


function getSecondLargest(nums) {
    // Complete the functionMath.min.apply(null, arr)
   const a= Math.max.apply(null,nums);
    const result = nums.filter(word => word< a);

    b=Math.max.apply(null,result);

    return b;



}
const aa=getSecondLargest([4,5,3,2,3,5,6,9])
console.log(aa)