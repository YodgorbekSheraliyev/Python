function calculate(nums) {
  let sum = 0;
  let isStart = false;
  nums.forEach((num) => {
    if (num == 6) {
      isStart = true;
    }
    if(!isStart){
      sum +=num
    }
    if ( num == 7) {
      isStart = false;
    }
  });
  console.log(sum);

  return sum;
}

calculate([1, 6, 5, 5, 7, 8]);
// console.log(result);
