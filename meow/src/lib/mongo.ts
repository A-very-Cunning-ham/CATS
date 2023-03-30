import {MongoClient} from 'mongodb';

// TODO: generate these values using .env

const client = new MongoClient('mongodb+srv://william:12345@cluster0.2nxfqjy.mongodb.net/?retryWrites=true&w=majority')

export function start_mongo() {
	console.log('Starting mongo...');
	return client.connect();
}

export default client.db('mongodbVSCodePlaygroundDB')