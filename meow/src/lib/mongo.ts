import {MongoClient} from 'mongodb';

// TODO: generate these values using .env

const client = new MongoClient('mongodb://root:123456@mongodb:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true')

export function start_mongo() {
	console.log('Starting mongo...');
	return client.connect();
}

export default client.db('CATS')