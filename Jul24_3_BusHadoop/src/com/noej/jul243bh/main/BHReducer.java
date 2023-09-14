package com.noej.jul243bh.main;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class BHReducer extends Reducer<Text, LongWritable, Text, LongWritable>{
	
	private static final LongWritable SUM = new LongWritable();
	
	@Override
	protected void reduce(Text arg0, Iterable<LongWritable> arg1,
			Reducer<Text, LongWritable, Text, LongWritable>.Context arg2) throws IOException, InterruptedException {
		long sum = 0;
		for (LongWritable l : arg1) {
			sum += l.get();
		}
		SUM.set(sum);
		arg2.write(arg0,  SUM);
	}
	
}
