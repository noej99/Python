package com.noej.jul272sh.main;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class SHMapper extends Mapper<Object, Text, Text, IntWritable> {
	
	private static final Text WORD = new Text();
	private static final IntWritable ZERO = new IntWritable(0);
	
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
		StringTokenizer st = new StringTokenizer(value.toString(), " ");
		while (st.hasMoreTokens()) {
			WORD.set(st.nextToken());
			context.write(WORD, ZERO);
		}
	}
}
