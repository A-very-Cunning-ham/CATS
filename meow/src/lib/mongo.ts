import {MongoClient} from 'mongodb';

// TODO: generate these values using .env

const client = new MongoClient('')

export function start_mongo() {
	console.log('Starting mongo...');
	return client.connect();
}

export default client.db('demo')
