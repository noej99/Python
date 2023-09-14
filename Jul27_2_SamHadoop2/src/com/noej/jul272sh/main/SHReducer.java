package com.noej.jul272sh.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class SHReducer extends Reducer<Text, IntWritable, Text, IntWritable>{

	private static final IntWritable ZERO = new IntWritable(0);
	
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException {
		
		arg2.write(arg0, ZERO);
		
	}
}
