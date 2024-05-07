// 최대공약수 찾기
function findGcd(a, b) {
    return b === 0 ? a : findGcd(b, a % b)
}

function solution(numer1, denom1, numer2, denom2) {
    const sumDenom = denom1 * denom2;
    const sumNumer = numer1 * denom2 + numer2 * denom1;
    const gcd = findGcd(sumDenom, sumNumer);
    return [sumNumer/gcd, sumDenom/gcd];
}