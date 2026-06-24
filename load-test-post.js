import http from 'k6/http';
import { check } from 'k6'

export const options = {
    vus: 10,
    duration: '10s',
};

export default function () {
    const url = 'https://jsonplaceholder.typicode.com/posts';
    const payload = JSON.stringify({
        title: 'Testovaci clanok',
        body: 'Toto je testovaci clanok z k6',
        userId: 1,
    });
    const params = {
        headers: {
            'Content-Type': 'aplication/json',
        },
    };
    const res = http.post(url, payload, params);
    check(res,{
        'status is 201': (r) => r.status === 201,
    });
}