package com.noej.jul252sh.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class SHReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
	private static final IntWritable SUM = new IntWritable();
	
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException {
		int sum = 0;
		for (IntWritable i : arg1) {
			sum += i.get();
		}
		SUM.set(sum);
		arg2.write(arg0, SUM);
	}
}
