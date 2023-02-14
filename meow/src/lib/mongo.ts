import {MongoClient} from 'mongodb';

const client = new MongoClient('mongodb+srv://william:123@cluster0.2nxfqjy.mongodb.net/?retryWrites=true&w=majority')

export function start_mongo() {
	console.log('Starting mongo...');
	return client.connect();
}

export default client.db('mongodbVSCodePlaygroundDB')