import { NextApiRequest, NextApiResponse } from 'next';
import { promisify } from 'util';
import { exec } from 'child_process';

const execAsync = promisify(exec);

export default async function handler(req, res) {
  // Execute the monitoring script
  try {
    await execAsync('python src/monitor.py');
    res.status(200).json({ message: 'Monitoring executed successfully.' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
} 