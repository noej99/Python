package com.noej.jul252kh.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class KHMapper extends Mapper<Object, Text, Text, IntWritable> {
	private static final Text WHO = new Text();
	private static final IntWritable ONE = new IntWritable();

	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
		try {
			String line = value.toString();
			
			if (line.startsWith("2023년")) {
				String[] line2 = line.split(" : ");
				String[] line3 = line2[0].split(", ");
				WHO.set(line3[1]);
				context.write(WHO, ONE);
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
