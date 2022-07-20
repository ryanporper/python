/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */

 function dedupeSorted(num) {
    let arr = [num[0]]
    // console.log(arr)
    for (i=1; i<num.length; i++){
        if (num[i] != num[i-1]){
            arr.push(num[i])
            // console.log(arr)
        }
        // else return arr
    }
    return arr
}

console.log(dedupeSorted(nums1)); // [1]
console.log(dedupeSorted(nums2)); // [1, 2, 3]
console.log(dedupeSorted(nums3)); // [1, 2, 3, 4]
console.log(dedupeSorted(nums4)); // [1]

console.log(dedupeSorted(nums1)); // [1]
console.log(dedupeSorted(nums2)); // [1, 2, 3]
console.log(dedupeSorted(nums3)); // [1, 2, 3, 4]
console.log(dedupeSorted(nums4)); // [1]

/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const numsA = [3, 5, 4, 3, 4, 6, 5];
const expectedA = 6;

const numsB = [3, 5, 5];
const expectedB = 3;

const numsC = [3, 3, 5];
const expectedC = 5;

const numsD = [5];
const expectedD = 5;

const numsE = [];
const expectedE = null;

const numsF = [1,4,5,5,6,6]
const expectedF = 1;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {
    let num = nums[0]

    for(i=0;i<nums.length;i++){
        if(nums[0] != nums[i]) {
            return  
        }
    }
}
console.log(firstNonRepeated(numsA)); // 6
console.log(firstNonRepeated(numsB)); // 3
console.log(firstNonRepeated(numsC)); // 5
console.log(firstNonRepeated(numsD)); // 5
console.log(firstNonRepeated(numsE)); // null
console.log(firstNonRepeated(numsF)); // 1