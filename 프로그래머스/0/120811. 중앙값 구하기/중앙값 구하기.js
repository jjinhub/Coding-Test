function solution(array) {
    var answer = 0;
    const sortArray = array.sort((a, b) => (a - b));
    console.log(sortArray)
    const centerIndex = Math.floor(sortArray.length / 2);
    answer = sortArray[centerIndex];
    return answer;
}