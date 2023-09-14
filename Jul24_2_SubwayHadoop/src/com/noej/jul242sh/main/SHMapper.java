package com.noej.jul242sh.main;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class SHMapper extends Mapper<Object, Text, Text, LongWritable> {
	
	private static final Text NO = new Text();
//	private static final LongWritable RIDE = new LongWritable();
	private static final LongWritable ALIGHT = new LongWritable();
	
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, LongWritable>.Context context)
			throws IOException, InterruptedException {
		String[] line = value.toString().split(",");
		NO.set(line[3]);
//		RIDE.set(Long.parseLong(line[5]));
//		context.write(NO, RIDE);
		ALIGHT.set(Long.parseLong(line[6]));
		context.write(NO, ALIGHT);
	}
}
